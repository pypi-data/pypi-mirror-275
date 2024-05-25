import asyncio
import time
from typing import Any, Dict

import pytest

from openlimit_lite import ChatRateLimiter

rate_limiter_async = ChatRateLimiter(request_limit=200, token_limit=4000)

rate_limiter_sync = ChatRateLimiter(request_limit=200, token_limit=4000)


@pytest.fixture(scope="module")
def chat_params() -> Dict[str, Any]:
    return {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
        ],
        "max_tokens": 1,
        "n": 1,
    }


def test_rate_limiter_sync(chat_params: Dict[str, Any]):
    start_time = time.time()
    duration = 5  # seconds
    successful_calls = 0

    while (time.time() - start_time) < duration:
        with rate_limiter_sync.limit(**chat_params):
            successful_calls += 1

    # Check if the number of successful calls is within the rate limits
    assert 0 < successful_calls <= rate_limiter_sync.request_limit * (duration / 60)


async def rate_limited_function_async(chat_params: Dict[str, Any]):
    async with rate_limiter_async.limit(**chat_params):
        # do something
        return "success"


@pytest.mark.asyncio
async def test_rate_limiter_within_limits_async(chat_params: Dict[str, Any]):
    async def run_rate_limited_function():
        try:
            await rate_limited_function_async(chat_params)
            return 1
        except Exception as e:
            print(e)
            return 0

    async def count_successful_calls(duration: int):
        start_time = asyncio.get_event_loop().time()
        count = 0
        while (asyncio.get_event_loop().time() - start_time) < duration:
            count += await run_rate_limited_function()
        return count

    duration = 5  # seconds
    successful_calls = await count_successful_calls(duration)

    # Check if the number of successful calls is within the rate limits
    assert 0 < successful_calls <= rate_limiter_async.request_limit * (duration / 60)
