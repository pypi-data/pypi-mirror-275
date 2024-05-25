# Standard library
from functools import wraps
from inspect import iscoroutinefunction
from typing import (
    Awaitable,
    Callable,
    Dict,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Any,
    Union,
    cast,
)

from openlimit_lite.rate_limiters import RateLimiter

F = TypeVar("F", bound=Union[Callable[..., Any], Callable[..., Awaitable[Any]]])


######
# MAIN
######


class FunctionDecorator(object):
    """
    Converts rate limiter into a function decorator.
    """

    def __init__(self, rate_limiter: "RateLimiter"):
        self.rate_limiter = rate_limiter

    def __call__(self, func: F) -> F:

        @wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]):
            if iscoroutinefunction(func):

                async def async_wrapper(
                    *args: Tuple[Any, ...], **kwargs: Dict[str, Any]
                ):
                    async with self.rate_limiter.limit(**kwargs):
                        return await func(*args, **kwargs)

                return async_wrapper
            else:
                with self.rate_limiter.limit(**kwargs):
                    return func(*args, **kwargs)

        return cast(F, wrapper)


class ContextManager:
    """
    Converts rate limiter into context manager.
    """

    def __init__(self, num_tokens: int, rate_limiter: "RateLimiter"):
        self.num_tokens = num_tokens
        self.rate_limiter = rate_limiter

    def __enter__(self):
        self.rate_limiter.wait_for_capacity_sync(self.num_tokens)

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[Type[BaseException]],
    ) -> Optional[bool]:
        return False

    async def __aenter__(self):
        await self.rate_limiter.wait_for_capacity(self.num_tokens)

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[Type[BaseException]],
    ) -> Optional[bool]:
        return False
