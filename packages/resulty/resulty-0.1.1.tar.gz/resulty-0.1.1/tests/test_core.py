# ruff: noqa: TRY003, EM101, ARG005, PT011

import sys

sys.path.append("..")

import pytest

from src.resulty import (
    Err,
    Ok,
    PropagatedResultException,
    Result,
    ResultException,
    async_propagate_result,
    propagate_result,
)


def test_from_throwable_ok():
    def success_func():
        return 42

    result = Result.from_throwable(success_func)
    assert result.is_ok()
    assert result.value == 42


def test_from_throwable_err():
    def error_func():
        raise ValueError("Something went wrong")

    result = Result.from_throwable(error_func)
    assert result.is_err()
    assert isinstance(result.error, ValueError)
    assert str(result.error) == "Something went wrong"


@pytest.mark.asyncio
async def test_from_async_throwable_ok():
    async def success_async_func():
        return 42

    result = await Result.from_async_throwable(success_async_func)
    assert result.is_ok()
    assert result.value == 42


@pytest.mark.asyncio
async def test_from_async_throwable_err():
    async def error_async_func():
        raise ValueError("Something went wrong")

    result = await Result.from_async_throwable(error_async_func)
    assert result.is_err()
    assert isinstance(result.error, ValueError)
    assert str(result.error) == "Something went wrong"


def test_is_ok_and():
    ok_result = Ok(42)
    assert ok_result.is_ok_and(lambda x: x > 0)
    assert not ok_result.is_ok_and(lambda x: x < 0)

    err_result = Err("Error")
    assert not err_result.is_ok_and(lambda x: True)


def test_is_err_and():
    err_result = Err("Error")
    assert err_result.is_err_and(lambda x: len(x) > 0)
    assert not err_result.is_err_and(lambda x: len(x) == 0)

    ok_result = Ok(42)
    assert not ok_result.is_err_and(lambda x: True)


def test_ok():
    ok_result = Ok(42)
    assert ok_result.ok() == 42

    err_result = Err("Error")
    assert err_result.ok() is None


def test_err():
    err_result = Err("Error")
    assert err_result.err() == "Error"

    ok_result = Ok(42)
    assert ok_result.err() is None


def test_expect():
    ok_result = Ok(42)
    assert ok_result.expect("Should not raise") == 42

    err_result = Err("Error")
    with pytest.raises(ResultException) as exc_info:
        err_result.expect("Expected error")
    assert str(exc_info.value) == "ResultException: Expected error\nErr(Error)"


def test_expect_err():
    err_result = Err("Error")
    assert err_result.expect_err("Should not raise") == "Error"

    ok_result = Ok(42)
    with pytest.raises(ResultException) as exc_info:
        ok_result.expect_err("Expected ok")
    assert str(exc_info.value) == "ResultException: Expected ok\nOk(42)"


def test_unwrap():
    ok_result = Ok(42)
    assert ok_result.unwrap() == 42

    err_result = Err("Error")
    with pytest.raises(Exception) as exc_info:
        err_result.unwrap()
    assert (
        str(exc_info.value) == "ResultException: called `.unwrap()` on an `Err` value\nErr(Error)"
    )


def test_unwrap_err():
    err_result = Err("Error")
    assert err_result.unwrap_err() == "Error"

    ok_result = Ok(42)
    with pytest.raises(Exception) as exc_info:
        ok_result.unwrap_err()
    assert str(exc_info.value) == "ResultException: called `.unwrap_err()` on an `Ok` value\nOk(42)"


def test_unwrap_or():
    ok_result = Ok(42)
    assert ok_result.unwrap_or(0) == 42

    err_result = Err("Error")
    assert err_result.unwrap_or(0) == 0


def test_map():
    ok_result = Ok(42)
    mapped_result = ok_result.map(lambda x: x * 2)
    assert mapped_result.is_ok()
    assert mapped_result.value == 84

    err_result = Err("Error")
    mapped_result = err_result.map(lambda x: x * 2)
    assert mapped_result.is_err()
    assert mapped_result.error == "Error"


def test_map_err():
    ok_result = Ok(42)
    mapped_result = ok_result.map_err(lambda x: f"Mapped {x}")
    assert mapped_result.is_ok()
    assert mapped_result.value == 42

    err_result = Err("Error")
    mapped_result = err_result.map_err(lambda x: f"Mapped {x}")
    assert mapped_result.is_err()
    assert mapped_result.error == "Mapped Error"


def test_map_or():
    ok_result = Ok(42)
    assert ok_result.map_or(0, lambda x: x * 2) == 84

    err_result = Err("Error")
    assert err_result.map_or(0, lambda x: x * 2) == 0


def test_map_or_else():
    ok_result = Ok(42)
    assert ok_result.map_or_else(lambda x: len(x), lambda x: x * 2) == 84

    err_result = Err("Error")
    assert err_result.map_or_else(lambda x: len(x), lambda x: x * 2) == 5


def test_inspect():
    ok_result = Ok(42)
    inspect_calls = []
    result = ok_result.inspect(lambda x: inspect_calls.append(x))
    assert result == ok_result
    assert inspect_calls == [42]

    err_result = Err("Error")
    inspect_calls = []
    result = err_result.inspect(lambda x: inspect_calls.append(x))
    assert result == err_result
    assert inspect_calls == []


def test_propagate_result_ok():
    @propagate_result
    def success_func():
        return Ok(42)

    result = success_func()
    assert result.is_ok()
    assert result.value == 42


def test_propagate_result_err():
    @propagate_result
    def error_func():
        return Err("Error")

    result = error_func()
    assert result.is_err()
    assert result.error == "Error"


def test_propagate_result_exception():
    @propagate_result
    def exception_func():
        raise PropagatedResultException(Err("Propagated Error"))

    result = exception_func()
    assert result.is_err()
    assert result.error == "Propagated Error"


@pytest.mark.asyncio
async def test_async_propagate_result_ok():
    @async_propagate_result
    async def success_async_func():
        return Ok(42)

    result = await success_async_func()
    assert result.is_ok()
    assert result.value == 42


@pytest.mark.asyncio
async def test_async_propagate_result_err():
    @async_propagate_result
    async def error_async_func():
        return Err("Error")

    result = await error_async_func()
    assert result.is_err()
    assert result.error == "Error"


@pytest.mark.asyncio
async def test_async_propagate_result_exception():
    @async_propagate_result
    async def exception_async_func():
        raise PropagatedResultException(Err("Propagated Error"))

    result = await exception_async_func()
    assert result.is_err()
    assert result.error == "Propagated Error"


def test_up_ok():
    ok_result = Ok(42)
    assert ok_result.up() == 42


def test_up_err():
    err_result = Err("Error")
    with pytest.raises(PropagatedResultException) as exc_info:
        err_result.up()
    assert isinstance(exc_info.value, PropagatedResultException)
    assert exc_info.value.inner == err_result


def test_up_with_propagate_result():
    @propagate_result
    def success_func():
        im_good = Ok(42).up()
        return Ok(im_good)

    result = success_func()
    assert result.is_ok()
    assert result.value == 42

    @propagate_result
    def error_func():
        im_good = Ok(42).up()
        im_not_good = Err("Error").up()  # noqa: F841
        return Ok(im_good)

    result = error_func()
    assert result.is_err()
    assert result.error == "Error"


def test_and_also():
    ok_result = Ok(42)
    other_result = Ok("Hello")
    assert ok_result.and_also(other_result) == other_result

    err_result = Err("Error")
    other_result = Ok("Hello")
    assert err_result.and_also(other_result) == err_result


def test_and_then():
    ok_result = Ok(42)
    assert ok_result.and_then(lambda x: Ok(x * 2)) == Ok(84)
    assert ok_result.and_then(lambda x: Err("Error")) == Err("Error")

    err_result = Err("Error")
    assert err_result.and_then(lambda x: Ok(x * 2)) == Err("Error")


def test_or_if():
    ok_result = Ok(42)
    other_result = Ok(0)
    assert ok_result.or_if(other_result) == ok_result

    err_result = Err("Error")
    other_result = Ok(0)
    assert err_result.or_if(other_result) == other_result

    err_result = Err("Error")
    other_err_result = Err("Other Error")
    assert err_result.or_if(other_err_result) == other_err_result


def test_or_else():
    ok_result = Ok(42)
    assert ok_result.or_else(lambda x: Ok(0)) == ok_result

    err_result = Err("Error")
    assert err_result.or_else(lambda x: Ok(0)) == Ok(0)
    assert err_result.or_else(lambda x: Err("Other Error")) == Err("Other Error")


def test_clone():
    ok_result = Ok(42)
    cloned_result = ok_result.clone()
    assert ok_result == cloned_result
    assert ok_result is not cloned_result

    err_result = Err("Error")
    cloned_result = err_result.clone()
    assert err_result == cloned_result
    assert err_result is not cloned_result


def test_inspect_err():
    ok_result = Ok(42)
    inspect_calls = []
    result = ok_result.inspect_err(lambda x: inspect_calls.append(x))
    assert result == ok_result
    assert inspect_calls == []

    err_result = Err("Error")
    inspect_calls = []
    result = err_result.inspect_err(lambda x: inspect_calls.append(x))
    assert result == err_result
    assert inspect_calls == ["Error"]


def test_unwrap_or_else():
    ok_result = Ok(42)
    assert ok_result.unwrap_or_else(lambda x: 0) == 42

    err_result = Err("Error")
    assert err_result.unwrap_or_else(lambda x: len(x)) == 5
