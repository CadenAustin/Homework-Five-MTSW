import pytest
from functions import numbers

@pytest.mark.parametrize("dividend,divisor,quotient", [(30, 5, 6.0), (2, -1, -2.0), (-20, -5, 4.0), (1, 4, 0.25)])
def test_number_success(dividend, divisor, quotient):
    assert numbers(dividend, divisor) == quotient

def test_number_by_zero():
    with pytest.raises(ZeroDivisionError):
        numbers(1, 0)

def test_number_with_floats():
    assert numbers(0.25, 0.25) == 1

def test_numbers_with_bad_input():
    with pytest.raises(TypeError):
        numbers("hello", 0.25)