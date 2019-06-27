import math_func
import pytest

"""
def test_add():
    assert math_func.add(7, 3) == 10

def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'


def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36
"""

@pytest.mark.parametrize('num1, num2, result',
                         [(7, 3, 10),
                          ('Hello', ' World', 'Hello World'),
                          (10.5, 25.5, 36)
                         ])
def test_add(num1,num2,result):
    assert math_func.add(num1, num2) == result


