import pytest
from functions import sq

@pytest.mark.parametrize("num,result", [(4, 2), (9, 3), (20, 4.47213595499958)])
def test_sq_success(num, result):
    assert sq(num) == result

@pytest.mark.parametrize("num,result", [(4.8, 2.1908902300206643), (9.0, 3), (15.75, 3.968626966596886)])
def test_sq_with_floats(num, result):
    assert sq(num) == result

def test_sq_with_negative():
    with pytest.raises(ValueError):
        sq(-1)