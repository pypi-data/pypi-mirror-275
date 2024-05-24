import copy
from collections.abc import Awaitable, Callable
from typing import Any


class ResultException[T, E](Exception):  # noqa: N818
    """
    Represents an exception that occurs when trying to unwrap a Result object.

    Args:
        inner (Result[T, E]): The Result object that caused the exception.
        expect_msg (Optional[str]): An optional message to include in the exception.

    Examples:
        >>> result = Err("Error message")
        >>> try:
        ...     result.expect(
        ...         "Something went wrong"
        ...     )
        ... except ResultException as e:
        ...     print(str(e))
        ResultException: Something went wrong
        Err(Error message)
    """

    inner: "Result[T,E]"
    expect_msg = None

    def __init__(self, inner: "Result[T,E]", expect_msg: str | None = None):
        self.inner = inner
        self.expect_msg = expect_msg

    def __str__(self):
        return f"ResultException: {self.expect_msg}\n{self.inner}"


class PropagatedResultException[T, E](Exception):  # noqa: N818
    """
    Represents an exception that occurs when trying to propagate a Result object.

    Args:
        inner (Result[T, E]): The Result object that caused the exception.

    Examples:
        >>> @propagate_result
        ... def some_function():
        ...     result = Err(
        ...         "Error message"
        ...     )
        ...     return result.up()
        >>> try:
        ...     some_function()
        ... except (
        ...     PropagatedResultException
        ... ) as e:
        ...     print(str(e))
        PropagatedResultException: Err(Error message)
        Did you forget to use the propagate_result decorator?
    """

    inner: "Result[T,E]"

    def __init__(self, inner: "Result[T,E]"):
        self.inner = inner

    def __str__(self):
        return f"PropagatedResultException: {self.inner}\nDid you forget to use the propagate_result decorator?"


class Result[T, E]:
    """
    Represents a result that can either be an Ok value or an Err value.

    Args:
        value (T): The value of the Ok result.
        error (E): The value of the Err result.

    Examples:
        >>> ok_result = Result(42, None)
        >>> err_result = Result(
        ...     None, "Error message"
        ... )
    """

    def __init__(self, value: T, error: E):
        self.value = value
        self.error = error

    @staticmethod
    def from_throwable(f: Callable[[], T]) -> "Result[T, Exception]":
        """
        Creates a Result object from a function that may throw an exception.

        Args:
            f (Callable[[], T]): A callable that may throw an exception.

        Returns:
            Result[T, Exception]: A Result object with the result of the function, or an exception if one was thrown.

        Examples:
            >>> def division(a, b):
            ...     return a / b
            >>> result = (
            ...     Result.from_throwable(
            ...         lambda: division(
            ...             10, 2
            ...         )
            ...     )
            ... )
            >>> result
            Ok(5.0)
            >>> result = (
            ...     Result.from_throwable(
            ...         lambda: division(
            ...             10, 0
            ...         )
            ...     )
            ... )
            >>> result
            Err(division by zero)
        """
        try:
            return Ok(f())
        except Exception as e:  # noqa: BLE001
            return Err(e)

    @staticmethod
    async def from_async_throwable(f: Callable[[], Awaitable[T]]) -> "Result[T, Exception]":
        """
        Creates a Result object from an async function that may throw an exception.

        Args:
            f (Callable[[], Awaitable[T]]): An async callable that may throw an exception.

        Returns:
            Result[T, Exception]: A Result object with the result of the function, or an exception if one was thrown.

        Examples:
            >>> import asyncio
            >>> async def async_division(
            ...     a, b
            ... ):
            ...     return a / b
            >>> result = asyncio.run(
            ...     Result.from_async_throwable(
            ...         lambda: async_division(
            ...             10, 2
            ...         )
            ...     )
            ... )
            >>> result
            Ok(5.0)
            >>> result = asyncio.run(
            ...     Result.from_async_throwable(
            ...         lambda: async_division(
            ...             10, 0
            ...         )
            ...     )
            ... )
            >>> result
            Err(division by zero)
        """
        try:
            return Ok(await f())
        except Exception as e:  # noqa: BLE001
            return Err(e)

    def is_ok(self) -> bool:
        """
        Checks if the result is Ok.

        Returns:
            bool: True if the result is Ok, False otherwise.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.is_ok()
            True
            >>> err_result = Err("Error")
            >>> err_result.is_ok()
            False
        """
        return self.error is None

    def is_ok_and(self, f: Callable[[T], bool]) -> bool:
        """
        Checks if the result is Ok and the value satisfies the given predicate.

        Args:
            f (Callable[[T], bool]): A callable that takes the value of the result and returns a boolean.

        Returns:
            bool: True if the result is Ok and the value satisfies the predicate, False otherwise.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.is_ok_and(
            ...     lambda x: x > 0
            ... )
            True
            >>> ok_result.is_ok_and(
            ...     lambda x: x < 0
            ... )
            False
            >>> err_result = Err("Error")
            >>> err_result.is_ok_and(
            ...     lambda x: True
            ... )
            False
        """
        return self.error is None and f(self.value)

    def is_err(self) -> bool:
        """
        Checks if the result is an Err.

        Returns:
            bool: True if the result is an Err, False otherwise.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.is_err()
            False
            >>> err_result = Err("Error")
            >>> err_result.is_err()
            True
        """
        return self.error is not None

    def is_err_and(self, f: Callable[[E], bool]) -> bool:
        """
        Checks if the result is an Err and the error satisfies the given predicate.

        Args:
            f (Callable[[E], bool]): A callable that takes the error value and returns a boolean.

        Returns:
            bool: True if the result is an Err and the error satisfies the predicate, False otherwise.

        Examples:
            >>> err_result = Err("Error")
            >>> err_result.is_err_and(
            ...     lambda x: len(x) > 0
            ... )
            True
            >>> err_result.is_err_and(
            ...     lambda x: len(x) == 0
            ... )
            False
            >>> ok_result = Ok(42)
            >>> ok_result.is_err_and(
            ...     lambda x: True
            ... )
            False
        """
        return self.error is not None and f(self.error)

    def ok(self) -> "T | None":
        """
        Returns the value if the result is Ok, otherwise returns None.

        Returns:
            Optional[T]: The value if the result is Ok, otherwise None.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.ok()
            42
            >>> err_result = Err("Error")
            >>> err_result.ok() is None
            True
        """
        if self.is_ok():
            return self.value
        return None

    def err(self) -> "E | None":
        """
        Returns the error value if the result is an Err, otherwise returns None.

        Returns:
            Optional[E]: The error value if the result is an Err, otherwise None.

        Examples:
            >>> err_result = Err("Error")
            >>> err_result.err()
            'Error'
            >>> ok_result = Ok(42)
            >>> ok_result.err() is None
            True
        """
        if self.is_err():
            return self.error
        return None

    def expect(self, msg: str) -> T:
        """
        Unwraps the value from the Result if it is not an Err.
        If the Result is an Err, raises a ResultException with the given message.

        Args:
            msg (str): The message to include in the exception if the Result is an Err.

        Returns:
            T: The unwrapped value.

        Raises:
            ResultException: If the Result is an Err.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.expect(
            ...     "Something went wrong"
            ... )
            42
            >>> err_result = Err("Error")
            >>> try:
            ...     err_result.expect(
            ...         "Something went wrong"
            ...     )
            ... except ResultException as e:
            ...     print(str(e))
            ResultException: Something went wrong
            Err(Error)
        """
        if self.is_err():
            raise ResultException(self, msg)
        return self.value

    def expect_err(self, msg: str) -> E:
        """
        Unwraps the error value from the Result if it is an Err.
        If the Result is Ok, raises a ResultException with the given message.

        Args:
            msg (str): The message to include in the exception if the Result is Ok.

        Returns:
            E: The unwrapped error value.

        Raises:
            ResultException: If the Result is Ok.

        Examples:
            >>> err_result = Err("Error")
            >>> err_result.expect_err(
            ...     "Something went wrong"
            ... )
            'Error'
            >>> ok_result = Ok(42)
            >>> try:
            ...     ok_result.expect_err(
            ...         "Something went wrong"
            ...     )
            ... except ResultException as e:
            ...     print(str(e))
            ResultException: Something went wrong
            Ok(42)
        """
        if self.is_ok():
            raise ResultException(self, msg)
        return self.error

    def unwrap(self) -> T:
        """
        Unwraps the value from the Result if it is not an Err.

        Returns:
            T: The unwrapped value.

        Raises:
            ResultException: If the Result is an Err.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.unwrap()
            42
            >>> err_result = Err("Error")
            >>> try:
            ...     err_result.unwrap()
            ... except ResultException as e:
            ...     print(str(e))
            ResultException: called `.unwrap()` on an `Err` value
            Err(Error)
        """
        if self.is_err():
            raise ResultException(self, "called `.unwrap()` on an `Err` value")
        return self.value

    def unwrap_err(self) -> E:
        """
        Unwraps the error value from the Result if it is an Err.

        Returns:
            E: The unwrapped error value.

        Raises:
            ResultException: If the Result is Ok.

        Examples:
            >>> err_result = Err("Error")
            >>> err_result.unwrap_err()
            'Error'
            >>> ok_result = Ok(42)
            >>> try:
            ...     ok_result.unwrap_err()
            ... except ResultException as e:
            ...     print(str(e))
            ResultException: called `.unwrap_err()` on an `Ok` value
            Ok(42)
        """
        if self.is_ok():
            raise ResultException(self, "called `.unwrap_err()` on an `Ok` value")
        return self.error

    def unwrap_or(self, default: T) -> T:
        """
        Unwraps the value from the Result if it is Ok, otherwise returns the provided default value.

        Args:
            default (T): The default value to return if the Result is an Err.

        Returns:
            T: The unwrapped value if the Result is Ok, otherwise the default value.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.unwrap_or(0)
            42
            >>> err_result = Err("Error")
            >>> err_result.unwrap_or(0)
            0
        """
        if self.is_err():
            return default
        return self.value

    def unwrap_or_else(self, f: Callable[[E], T]) -> T:
        """
        Unwraps the value from the Result if it is Ok, otherwise calls the provided function with the error value.

        Args:
            f (Callable[[E], T]): The function to call with the error value if the Result is an Err.

        Returns:
            T: The unwrapped value if the Result is Ok, otherwise the result of calling the provided function.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.unwrap_or_else(
            ...     lambda e: len(e)
            ... )
            42
            >>> err_result = Err("Error")
            >>> err_result.unwrap_or_else(
            ...     lambda e: len(e)
            ... )
            5
        """
        if self.is_err():
            return f(self.error)
        return self.value

    def up(self) -> T:
        """
        Unwraps the value from the Result if it is Ok, otherwise propagates the error to the caller.
        This is meant to be used with the `@propagate_result` (or `@async_propagate_result`) decorator.

        Returns:
            T: The unwrapped value.

        Raises:
            PropagatedResultException: If the Result is an Err.

        Examples:
            >>> @propagate_result
            ... def some_function():
            ...     ok_result = Ok(42)
            ...     return ok_result.up()
            >>> some_function()
            Ok(42)
            >>> @propagate_result
            ... def another_function():
            ...     err_result = Err("Error")
            ...     return err_result.up()
            >>> another_function()
            Err(Error)
        """
        if self.is_err():
            raise PropagatedResultException(self)
        return self.value

    def map[U](self, f: Callable[[T], U]) -> "Result[U | T, E]":
        """
        Applies the given function `f` to the value contained in the `Result` object if it is Ok.
        If the `Result` object contains an error, it returns a new `Result` object with the same error.

        Args:
            f (Callable[[T], U]): A callable that takes a value of type `T` and returns a value of type `U`.

        Returns:
            Result[U | T, E]: A new `Result` object with the result of applying `f` to the value, or the same `Result` object with the error.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.map(lambda x: x * 2)
            Ok(84)
            >>> err_result = Err("Error")
            >>> err_result.map(
            ...     lambda x: x * 2
            ... )
            Err(Error)
        """
        if self.error is not None:
            return Result(self.value, self.error)
        return Result(f(self.value), self.error)

    def map_err[F](self, f: Callable[[E], F]) -> "Result[T, F | E]":
        """
        Applies the given function `f` to the error value of the Result if it is an Err.
        If the Result is Ok, the function is not applied and the Result is returned as is.

        Args:
            f (Callable[[E], F]): A callable that takes an error value of type `E` and returns a new error value of type `F`.

        Returns:
            Result[T, F | E]: A new Result object with the same value as the original Result, but with the error value transformed by `f` if it is an Err.
                              If the original Result is Ok, the new Result will have the same value and no error.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.map_err(
            ...     lambda x: f"Mapped {x}"
            ... )
            Ok(42)
            >>> err_result = Err("Error")
            >>> err_result.map_err(
            ...     lambda x: f"Mapped {x}"
            ... )
            Err(Mapped Error)
        """
        if self.error is None:
            return Result(self.value, self.error)
        return Result(self.value, f(self.error))

    def map_or[U](self, default: U, f: Callable[[T], U]) -> U:
        """
        Applies the given function `f` to the value contained in the Result object if it is Ok,
        otherwise returns the provided default value.

        Args:
            default (U): The default value to return if the Result is an Err.
            f (Callable[[T], U]): A callable that takes a value of type `T` and returns a value of type `U`.

        Returns:
            U: The result of applying `f` to the value if the Result is Ok, otherwise the default value.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.map_or(
            ...     0, lambda x: x * 2
            ... )
            84
            >>> err_result = Err("Error")
            >>> err_result.map_or(
            ...     0, lambda x: x * 2
            ... )
            0
        """
        if self.error is not None:
            return default
        return f(self.value)

    def map_or_else[U](self, default: Callable[[E], U], f: Callable[[T], U]) -> U:
        """
        Applies the given function `f` to the value contained in the Result object if it is Ok,
        otherwise applies the `default` function to the error value.

        Args:
            default (Callable[[E], U]): A callable that takes an error value of type `E` and returns a value of type `U`.
            f (Callable[[T], U]): A callable that takes a value of type `T` and returns a value of type `U`.

        Returns:
            U: The result of applying `f` to the value if the Result is Ok, otherwise the result of applying `default` to the error.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.map_or_else(
            ...     lambda x: len(x),
            ...     lambda x: x * 2,
            ... )
            84
            >>> err_result = Err("Error")
            >>> err_result.map_or_else(
            ...     lambda x: len(x),
            ...     lambda x: x * 2,
            ... )
            5
        """
        if self.error is not None:
            return default(self.error)
        return f(self.value)

    def inspect(self, f: Callable[[T], None]) -> "Result[T, E]":
        """
        Calls the given function `f` with the value contained in the Result object if it is Ok.
        Returns the Result object as is.

        Args:
            f (Callable[[T], None]): A callable that takes a value of type `T` and returns `None`.

        Returns:
            Result[T, E]: The Result object as is.

        Examples:
            >>> ok_result = Ok(42)
            >>> inspect_calls = []
            >>> ok_result.inspect(
            ...     lambda x: inspect_calls.append(
            ...         x
            ...     )
            ... )
            Ok(42)
            >>> inspect_calls
            [42]
            >>> err_result = Err("Error")
            >>> inspect_calls = []
            >>> err_result.inspect(
            ...     lambda x: inspect_calls.append(
            ...         x
            ...     )
            ... )
            Err(Error)
            >>> inspect_calls
            []
        """
        if self.error is None:
            f(self.value)
        return self

    def inspect_err(self, f: Callable[[E], None]) -> "Result[T, E]":
        """
        Calls the given function `f` with the error contained in the Result object if it is Err.
        Returns the Result object as is.

        Args:
            f (Callable[[E], None]): A callable that takes an error of type `E` and returns `None`.

        Returns:
            Result[T, E]: The Result object as is.

        Examples:
            >>> ok_result = Ok(42)
            >>> inspect_calls = []
            >>> ok_result.inspect_err(
            ...     lambda x: inspect_calls.append(
            ...         x
            ...     )
            ... )
            Ok(42)
            >>> inspect_calls
            []
            >>> err_result = Err("Error")
            >>> inspect_calls = []
            >>> err_result.inspect_err(
            ...     lambda x: inspect_calls.append(
            ...         x
            ...     )
            ... )
            Err(Error)
            >>> inspect_calls
            ['Error']
        """
        if self.error is not None:
            f(self.error)
        return self

    def and_also[U](self, res: "Result[U, E]") -> "Result[U, E]":
        """
        Returns the given Result object `res` if this Result object is Ok.
        Otherwise, returns this Result object as is.

        Args:
            res (Result[U, E]): A Result object to return if this Result object is Ok.

        Returns:
            Result[U, E]: The given Result object if this Result object is Ok, otherwise this Result object as is.

        Examples:
            >>> ok_result = Ok(42)
            >>> other_result = Ok("Hello")
            >>> ok_result.and_also(
            ...     other_result
            ... )
            Ok(Hello)
            >>> err_result = Err("Error")
            >>> other_result = Ok("Hello")
            >>> err_result.and_also(
            ...     other_result
            ... )
            Err(Error)
        """
        if res.error is not None:
            return res
        if self.error is not None:
            return Err(self.error)
        return res

    def and_then[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
        """
        Applies the given function `f` to the value contained in the Result object if it is Ok.
        If the Result object contains an error, it returns a new Result object with the same error.

        Args:
            f (Callable[[T], Result[U, E]]): A callable that takes a value of type `T` and returns a Result object of type `Result[U, E]`.

        Returns:
            Result[U, E]: A new Result object with the result of applying `f` to the value, or the same Result object with the error.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.and_then(
            ...     lambda x: Ok(x * 2)
            ... )
            Ok(84)
            >>> ok_result.and_then(
            ...     lambda x: Err("Error")
            ... )
            Err(Error)
            >>> err_result = Err("Error")
            >>> err_result.and_then(
            ...     lambda x: Ok(x * 2)
            ... )
            Err(Error)
        """
        if self.error is not None:
            return Err(self.error)
        return f(self.value)

    def or_if(self, res: "Result[T, E]") -> "Result[T, E]":
        """
        Returns the Result object of `self` if it is Ok,
        or `res` if it is Ok (In this order).
        Else returns the error of `res`.

        Args:
            res (Result[T, E]): A Result object to return if this Result object is Err.

        Returns:
            Result[T, E]: The Result object of `self` if it is Ok, or `res` if it is Ok.
                          Otherwise, returns the error of `res`.

        Examples:
            >>> ok_result = Ok(42)
            >>> other_result = Ok(0)
            >>> ok_result.or_if(other_result)
            Ok(42)
            >>> err_result = Err("Error")
            >>> other_result = Ok(0)
            >>> err_result.or_if(other_result)
            Ok(0)
            >>> err_result = Err("Error")
            >>> other_err_result = Err(
            ...     "Other Error"
            ... )
            >>> err_result.or_if(
            ...     other_err_result
            ... )
            Err(Other Error)
        """
        if self.error is not None:
            return res
        return self

    def or_else(self, f: Callable[[E], "Result[T, E]"]) -> "Result[T, E]":
        """
        Returns the Result object of `self` if it is Ok,
        or the Result object returned by applying `f` to the error of `self`.

        Args:
            f (Callable[[E], Result[T, E]]): A callable that takes an error value of type `E` and returns a Result object of type `Result[T, E]`.

        Returns:
            Result[T, E]: The Result object of `self` if it is Ok, or the Result object returned by applying `f` to the error of `self`.

        Examples:
            >>> ok_result = Ok(42)
            >>> ok_result.or_else(
            ...     lambda x: Ok(0)
            ... )
            Ok(42)
            >>> err_result = Err("Error")
            >>> err_result.or_else(
            ...     lambda x: Ok(0)
            ... )
            Ok(0)
            >>> err_result.or_else(
            ...     lambda x: Err(
            ...         "Other Error"
            ...     )
            ... )
            Err(Other Error)
        """
        if self.error is not None:
            return f(self.error)
        return self

    def clone(self) -> "Result[T, E]":
        """
        Creates a deep copy of the Result object.

        Returns:
            Result[T, E]: A deep copy of the Result object.

        Examples:
            >>> ok_result = Ok(42)
            >>> cloned_result = (
            ...     ok_result.clone()
            ... )
            >>> ok_result == cloned_result
            True
            >>> ok_result is cloned_result
            False
            >>> err_result = Err("Error")
            >>> cloned_result = (
            ...     err_result.clone()
            ... )
            >>> err_result == cloned_result
            True
            >>> err_result is cloned_result
            False
        """
        return Result(copy.deepcopy(self.value), copy.deepcopy(self.error))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Result):
            return False
        return self.value == other.value and self.error == other.error

    def __str__(self) -> str:
        if self.error is not None:
            return f"Err({self.error})"
        return f"Ok({self.value})"

    def __repr__(self) -> str:
        return self.__str__()


def Ok[T](inner: T) -> Result[T, Any]:  # noqa: N802
    """
    Creates a Result object with a successful outcome.

    Args:
        inner (T): The value to be wrapped inside the Result object.

    Returns:
        Result[T, Any]: A Result object representing a successful outcome with the given value.

    Examples:
        >>> Ok(42)
        Ok(42)
    """
    return Result(inner, None)


def Err[E](inner: E) -> Result[Any, E]:  # noqa: N802
    """
    Creates a Result object representing an error.

    Args:
        inner (E): The value representing the error.

    Returns:
        Result[Any, E]: A Result object with an error value.

    Examples:
        >>> Err("Error")
        Err(Error)
    """
    return Result(None, inner)
