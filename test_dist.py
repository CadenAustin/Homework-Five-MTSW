import pytest
from functions import dist

@pytest.mark.parametrize("second,expected", [((10, 10), 5), ((5, 17), 7), ((17, 6.5), 12.5), ((-2, -5), 16.55294535724685)])
def test_dist_success(second, expected):
    x1, y1 = (5, 10)
    x2, y2 = second

    assert dist(x1, y1, x2, y2) == expected

def test_dist_bad_points():
    x1, y1 = ("hello", "world")
    x2, y2 = ("world", "hello")

    with pytest.raises(TypeError):
        dist(x1, y1, x2, y2)