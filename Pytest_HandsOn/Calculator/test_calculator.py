import pytest
from calculator import Calculator,  CalculatorError

def test_add():
    # Arrange
    calculator = Calculator()   # my class
    # Act
    result = calculator.add(2, 3)
    # Assert
    assert result == 5

def test_add_weird_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add("two", 3) # it will be failed. So, we need to create an exception (raises)

def test_add_weirder_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add("two", "three") # it will be failed. So, we need to create an exception (raises)


def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(5, 3)
    assert result == 2

def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(9, 3)
    assert result == 27

def test_divide():
    calculator = Calculator()
    result = calculator.divide(9, 3)
    assert result == 3

def test_divide_zero():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 0)


