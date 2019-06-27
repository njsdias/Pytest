
## Parameterizing tests

In test_math_func.py file we have three test that call the test add three times.
It is not necessary once we parametrize our test. For this I comment the old test
and write new one parameterized.

In the new test function we pass three arguments (two to do the sum, and one for the result) using
the **parametrize** decorator. After these arguments I pass an iterable list where we can provide 
the values for the three arguments. This list is a tuple. 

    @pytest.mark.parametrize('arg1, arg2,..,argN', tuple)

After these arguments I pass an iterable list where we can provide the values for the three arguments.
 This list is a tuple. 