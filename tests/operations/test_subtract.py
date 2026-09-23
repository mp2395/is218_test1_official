from calculator import subtract
def test_subtract():
    assert subtract(10, 4) == 6
from calculator import subtract
def test_subtract_zero():
    assert subtract(7, 0) == 7
from calculator import subtract
def test_subtract_negative_result():
    assert subtract(-3, 2) == -5
