from collections.abc import Callable, Coroutine
from functools import wraps

from .core import PropagatedResultException, Result  # noqa: TID252


def propagate_result[T, E](f: Callable[..., Result[T, E]]) -> Callable[..., Result[T, E]]:
    """
    Decorator function that catches `PropagatedResultException` exceptions and returns the result.

    Args:
        f (Callable[..., Result[T, E]]): The function to be decorated.

    Returns:
        Callable[..., Result[T, E]]: The decorated function that returns a `Result` object.

    Examples:
        >>> @propagate_result
        ... def ok_function():
        ...     return Ok(42)
        >>> ok_function()
        Ok(42)
        >>> @propagate_result
        ... def err_function():
        ...     raise PropagatedResultException(
        ...         Err("Error")
        ...     )
        >>> err_function()
        Err(Error)
    """

    @wraps(f)
    def wrapper(*args, **kwargs) -> Result[T, E]:
        try:
            return f(*args, **kwargs)
        except PropagatedResultException as e:
            return e.inner

    return wrapper


def async_propagate_result[T, E](
    f: Callable[..., Coroutine[None, None, Result[T, E]]],
) -> Callable[..., Coroutine[None, None, Result[T, E]]]:
    """
    Decorator function that catches `PropagatedResultException` exceptions and returns the result.

    Args:
        f (Callable[..., Coroutine[None, None, Result[T, E]]]): The coroutine function to be decorated.

    Returns:
        Callable[..., Coroutine[None, None, Result[T, E]]]: The decorated coroutine function that returns a `Result` object.

    Examples:
        >>> import asyncio
        >>> @async_propagate_result
        ... async def async_ok_function():
        ...     return Ok(42)
        >>> asyncio.run(
        ...     async_ok_function()
        ... )
        Ok(42)
        >>> @async_propagate_result
        ... async def async_err_function():
        ...     raise PropagatedResultException(
        ...         Err("Error")
        ...     )
        >>> asyncio.run(
        ...     async_err_function()
        ... )
        Err(Error)
    """

    @wraps(f)
    async def wrapper(*args, **kwargs) -> Result[T, E]:
        try:
            return await f(*args, **kwargs)
        except PropagatedResultException as e:
            return e.inner

    return wrapper
