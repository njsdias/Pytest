import math_func
import pytest
import sys # used to demonstrate the skipif decorator
           # sys give us the python version
"""
Add decorator "mark" before each test to allow us run a specific group of tests
Here we have two marks: number and strings
pytest test_math_func.py -v -m number   #runs only test_add and test_prod
"""

"""
The option "-x" in the command pytest means "exit first". 
So, whenever first failure occurs  in your test the PI test will exit from the 
execution of your test
"""

"""
The option --tb=no disable the stack trace: only a few information appears when the test fails
"""

"""
The option --maxfail= Number it wait for the maximum number of failure and then it will exit 
"""

"""
The option -rsx shows the reason of skip
"""


@pytest.mark.number
#@pytest.mark.skip(reason="do not run number add test") # to not run this test
#@pytest.mark.skipif(sys.version_info < (3, 3), reason="do not run number add test") #This only skip if python version is low than 3.3
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7


@pytest.mark.number
def test_prod():
    assert math_func.prod(5, 5) == 25
    assert math_func.prod(5) == 10
    assert math_func.prod(7) == 14
    # assert math_func.prod(7) == 9  # the test will fails and with the option -x the test procedure will exit
                                     # to test -x and --maxfail

@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldlo' not in result

@pytest.mark.strings
def test_prod_strings():
    assert math_func.prod('Hello ', 3) == 'Hello Hello Hello '

    result = math_func.prod('Hello ')
    assert result == 'Hello Hello '

    assert type(result) is str
    assert 'Hello' in result


