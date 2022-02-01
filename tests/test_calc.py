import pytest

from src.d4_calc_with_pytest import divide, round_up, multiply, hypotenuse


def test_multiply():
    actual = multiply(4, 5)
    expected = 20
    assert actual == expected


def test_divide():
    actual = divide(4, 5)
    expected = 0.8
    assert actual == expected, "Should return something"


def test_divide_one_decimal():
    assert divide(2, 3) == 0.7


def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(1 / 0)


def test_round_up():
    assert round_up(2.2) == 3


def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²

            |\
          L | \
          e |  \
          g |   \
         (A)|    \
            ------
            Leg(B)

    3² + 4² = 5²
    9  + 16 = 25
    Hypotenuse (c) = 5.0
    """
    assert hypotenuse(3, 4) == 5