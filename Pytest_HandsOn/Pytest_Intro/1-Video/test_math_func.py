import math_func

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_prod():
    assert math_func.prod(5 ,5) == 25
    assert math_func.prod(5) == 10
    assert math_func.prod(7) == 14

