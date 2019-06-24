# Pytest to ML

This repo was builded following the seminar occured in 2017 in Portland: Best Testing Practices for Data Science PyCon 2017.

Please watch the [video](https://www.youtube.com/watch?v=yACtdj1_IxE) to understand the importance and the basic procedure in doing test in your ML code.


Advices:

- First : Build your tests inside of a file test_name.py

- Second : Build your functions inside a file datafuncs.py


Notes:

- Check the lines that are not tested yet (pip install pytest-cov):

    pytest --cov-report term-missing --cov

check the  [output test file](https://github.com/njsdias/Pytest/blob/master/Pytest_ML/0-Intro/3-output-bonus.txt)


- To know more about the **assert** statement consult the [site](https://www.programiz.com/python-programming/assert-statement)

    - Key Points to Remember
    
        - Assertions are the condition or boolean expression which are always supposed to be true in the code.
        
        - Assert statement takes an expression and optional message.
        
        - Assert statement is used to check types, values of argument and the output of the function.
        
        - Assert statement is used as debugging tool as it halts the program at the point where an error occurs.
