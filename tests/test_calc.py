import pytest

from src.d4_calc_with_pytest import divide, round_up, multiply


def test_multiply():
    actual = multiply(4, 5)
    expected = 20
    assert actual == expected


def test_divide():
    actual = divide(4, 5)
    expected = 0.8
    assert actual == expected


def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(1 / 0)


def test_round_up():
    assert round_up(2.2) == 3
