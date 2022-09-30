import pytest

from fibonacci import fib


# write one or more pytest functions below, they need to start with test_
def test_fib_with_negative_arguments():
    with pytest.raises(ValueError):
        fib(-1)


def test_fib_recursion_anchor():
    assert fib(0) == 0
    assert fib(1) == 1


@pytest.mark.parametrize("n, expected", [
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5)
])
def test_fib(n, expected):
    assert fib(n) == expected

