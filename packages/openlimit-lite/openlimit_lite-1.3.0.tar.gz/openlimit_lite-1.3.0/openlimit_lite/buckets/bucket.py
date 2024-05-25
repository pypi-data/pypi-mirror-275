# Standard library
import time
from typing import Optional

######
# MAIN
######


class Bucket:
    def __init__(self, rate_limit: float, bucket_size_in_seconds: float = 1):
        # Per-second rate limit
        self._rate_per_sec: float = rate_limit / 60

        # Capacity of the bucket
        self._capacity: float = rate_limit / 60 * bucket_size_in_seconds

        # The integration time of the bucket
        self._bucket_size_in_seconds: float = bucket_size_in_seconds

        # Last time the bucket capacity was checked
        self._last_checked: float = time.time()

    def get_capacity(self, current_time: Optional[float] = None) -> float:

        if current_time is None:
            current_time = time.time()

        time_passed = current_time - self._last_checked

        new_capacity = min(
            self._rate_per_sec * self._bucket_size_in_seconds,
            self._capacity + time_passed * self._rate_per_sec,
        )

        return new_capacity

    def set_capacity(self, new_capacity: float, current_time: float) -> None:
        self._last_checked = current_time
        self._capacity = new_capacity
