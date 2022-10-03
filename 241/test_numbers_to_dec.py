from cmath import exp
import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("nums", [(range(10)), (list(range(10))), (set(range(10)))])
def test_list_to_decimal_accepts_list_like(nums):
    list_to_decimal(nums)


@pytest.mark.parametrize(
    "nums",
    [
        ([True, False]),
        ([1.1, 2.2, 3.3]),
        ("test")
    ],
)
def test_list_to_decimal_throw_typeerror(nums):
    with pytest.raises(TypeError):
        list_to_decimal(nums)


@pytest.mark.parametrize(
    "nums",
    [
        (range(-1,10)),
        (range(20)),
        (range(1,12,2))
    ],
)
def test_list_to_decimal_throw_valueerror(nums):
    with pytest.raises(ValueError):
        list_to_decimal(nums)


@pytest.mark.parametrize("nums, expected", [
    ([1,7,5], 175),
    ([0,3,1,2], 312),
    ([3,0,5,1], 3051)
])
def test_list_to_decimal(nums, expected):
    assert list_to_decimal(nums) == expected