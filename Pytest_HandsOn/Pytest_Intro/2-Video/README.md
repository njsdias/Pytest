
Add decorator "mark" before each test to allow us run a specific group of tests
Here we have two marks: number and strings

    pytest test_math_func.py -v -m number   #runs only test_add and test_prod


The option "-x" in the command pytest means "exit first".
So, whenever first failure occurs  in your test the pytest will exit from the
execution of your test.

The option **--tb=no** disable the stack trace: only a few information appears when the test fails.

The option **--maxfail= Number** it wait for the maximum number of failure and then it will exit.

**Skip**

- The decorator @pytest.mark.skip(reason="give a reason") before the test do not run the test

- The decorator @pytest.mark.skipif(sys.version_info < (3, 3), reason=" give a reason")  before the test do not run 
the test if the python version is lower than 3.3

- The option **-rsx** shows the reason of skip.

