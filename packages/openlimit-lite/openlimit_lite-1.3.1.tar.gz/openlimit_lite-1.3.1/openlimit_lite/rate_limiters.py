# Standard library
from typing import Any, Callable, Dict

# Local
from openlimit_lite.utilities.token_counters import (
    num_tokens_consumed_by_chat_request,
    num_tokens_consumed_by_completion_request,
    num_tokens_consumed_by_embedding_request,
)
from openlimit_lite.buckets.bucket import Bucket
from openlimit_lite.buckets.buckets import Buckets

############
# BASE CLASS
############


class RateLimiter:
    def __init__(
        self,
        request_limit: int,
        token_limit: int,
        token_counter: Callable[..., int],
        bucket_size_in_seconds: float = 1,
    ):
        # Rate limits
        self.request_limit = request_limit
        self.token_limit = token_limit
        self.sleep_interval = 1 / (self.request_limit / 60)

        # Token counter
        self.token_counter = token_counter

        # Bucket size in seconds
        self._bucket_size_in_seconds = bucket_size_in_seconds

        # Buckets
        self._buckets = Buckets(
            buckets=[
                Bucket(request_limit, bucket_size_in_seconds),
                Bucket(token_limit, bucket_size_in_seconds),
            ]
        )

    async def wait_for_capacity(self, num_tokens: int):
        await self._buckets.wait_for_capacity(
            amounts=[1, num_tokens], sleep_interval=self.sleep_interval
        )

    def wait_for_capacity_sync(self, num_tokens: int):
        self._buckets.wait_for_capacity_sync(
            amounts=[1, num_tokens], sleep_interval=self.sleep_interval
        )

    def limit(self, **kwargs: Dict[str, Any]):
        num_tokens = self.token_counter(**kwargs)
        return ContextManager(num_tokens, self)

    def is_limited(self):
        return FunctionDecorator(self)


######
# MAIN
######


class ChatRateLimiter(RateLimiter):
    def __init__(
        self,
        request_limit: int = 3500,
        token_limit: int = 90000,
        bucket_size_in_seconds: float = 1,
    ):
        super().__init__(
            request_limit=request_limit,
            token_limit=token_limit,
            token_counter=num_tokens_consumed_by_chat_request,
            bucket_size_in_seconds=bucket_size_in_seconds,
        )


class CompletionRateLimiter(RateLimiter):
    def __init__(
        self,
        request_limit: int = 3500,
        token_limit: int = 350000,
        bucket_size_in_seconds: float = 1,
    ):
        super().__init__(
            request_limit=request_limit,
            token_limit=token_limit,
            token_counter=num_tokens_consumed_by_completion_request,
            bucket_size_in_seconds=bucket_size_in_seconds,
        )


class EmbeddingRateLimiter(RateLimiter):
    def __init__(
        self,
        request_limit: int = 3500,
        token_limit: int = 70000000,
        bucket_size_in_seconds: float = 1,
    ):
        super().__init__(
            request_limit=request_limit,
            token_limit=token_limit,
            token_counter=num_tokens_consumed_by_embedding_request,
            bucket_size_in_seconds=bucket_size_in_seconds,
        )


from openlimit_lite.utilities.context_decorators import (
    ContextManager,
    FunctionDecorator,
)
