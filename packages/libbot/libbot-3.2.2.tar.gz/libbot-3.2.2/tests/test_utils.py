from typing import Callable

import pytest

from libbot._utils import supports_argument


def func1(foo: str, bar: str):
    pass


def func2(foo: str):
    pass


@pytest.mark.parametrize(
    "func, arg_name, result",
    [
        (func1, "foo", True),
        (func2, "bar", False),
    ],
)
def test_supports_argument(func: Callable, arg_name: str, result: bool):
    assert supports_argument(func, arg_name) == result
