# pytest Fixtures

Fixtures are functions that are run by pytest before (and sometimes
after) the actual test functions. The code in the fixture can do whatever you
want it to. You can use fixtures to get a data set for the tests to work on. You
can use fixtures to get a system into a known state before running a test.
Fixtures are also used to get data ready for multiple tests.

Fixture functions often set up or retrieve some data that the test can work
with. Sometimes this data is considered a fixture. For example, the Django
community often uses fixture to mean some initial data that gets loaded into
a database at the start of an application.

The @pytest.fixture() decorator is used to tell pytest that a function is a fixture.
When you include the fixture name in the parameter list of a test function,
pytest knows to run it before running the test. Fixtures can do work, and can
also return data to the test function.

    import pytest
    
    @pytest.fixture()
    def some_data():
        """Return answer to ultimate question."""
        return 42

    def test_some_data(some_data):
        """Use fixture return value
        assert some_data == 42
        
You can put fixtures into individual test files, but to share fixtures among
multiple test files, you need to use a conftest.py file somewhere centrally located
for all of the tests. For the Tasks project, all of the fixtures will be in
tasks_proj/tests/conftest.py. Although conftest.py is a Python module, it should not be imported by test files.
**Don’t import conftest from anywhere.** The conftest.py file gets read by pytest, and is considered a local plugin.

**Note** pytest includes a cool fixture called _tmpdir_ that we can use for
testing and don’t have to worry about cleaning up. It’s not magic, just good
coding by the pytest folks.

- to see what’s running and when use _--setup-show_

        pytest --setup-show test_add.py -k valid_id
        
  Remember: The -k option enables you to pass in an expression to run tests that have
certain names specified by the expression as a substring of the test name.


Our test is in the middle, and pytest designates a SETUP and TEARDOWN portion
to each fixture. Going from test_add_returns_valid_id up, you see that tmpdir ran
before the test. And before that, tmpdir_factory. Apparently, tmpdir uses it as a
fixture. The F and S in front of the fixture names indicate scope. F for function scope,
and S for session scope.

Fixtures are a great place **to store data to use for testing**. You can return
anything. In _ch3/test_fixtures.py_ is a fixture that returns a tuple of mixed type.


## Using Multiple Fixtures (..\code\ch3\a\tasks_proj\tests\func>)

We want to test if when we add ONE task AFTER added THREE tasks the total of tasks is 4.
For this we have the follow fixtures:

- db_with_3_tasks(tasks_db, tasks_just_a_few) that use two fixtures (tasks_db, tasks_just_a_few).

- In the fixture task_just_a_few we defined THREE tasks. 

- In the fixture tasks_db we start the DataBase, do some tests and stop the DataBase.

In the test_add_increases_count(db_with_3_tasks) we use the fixture db_with_3_tasks to add the three tasks defined in the fixture tasks_just_a_few. After that we asssert if the tasks.count() == 4.

    def test_add_increases_count(db_with_3_tasks):               # db_with_3_tasks is ficture test defined in conftest.py
        """Test tasks.add() affect on tasks.count()."""
        # GIVEN a db with 3 tasks
        #  WHEN another task is added
         tasks.add(Task('throw a party'))

        #  THEN the count increases by 1
        assert tasks.count() == 4
        
 # Fixture Scope
 Fixtures include an optional parameter called scope, which controls how often
a fixture gets set up and torn down. The scopes are:

- scope='function': Run once per test function. The setup portion is run before each test using
the fixture. The teardown portion is run after each test using the fixture.
This is the default scope used when no scope parameter is specified.

- scope='class' : Run once per test class, regardless of how many test methods are in the class.

- scope='module' ; Run once per module, regardless of how many test functions or methods
or other fixtures in the module use it.

- scope='session' : Run once per session. All test methods and functions using a fixture of
session scope share one setup and teardown call.

So far, **if you wanted a test to use a fixture**, you put it in the parameter list.
You can also mark a test or a class with _@pytest.mark.usefixtures('fixture1', 'fixture2')_.
_usefixtures_ takes a string that is composed of a comma-separated list of fixtures
to use.

Using usefixtures is almost the same as specifying the fixture name in the test
method parameter list. **The one difference is** that the test can use the return
value of a fixture only if it’s specified in the parameter list. A test using a fixture
due to usefixtures cannot use the fixture’s return value.

The decision (in the code) of which database to use is isolated to the
start_tasks_db() call in the tasks_db_session fixture (ch3/b/tasks_proj/tests/conftest.py). To test MongoDB, we need to run all the tests with db_type set to mongo. A small
change does the trick (ch3/c/tasks_proj/tests/conftest.py)

    #@pytest.fixture(scope='session', params=['tiny',])
    @pytest.fixture(scope='session', params=['tiny', 'mongo'])
    def tasks_db_session(tmpdir_factory, request):
        """Connect to db before tests, disconnect after."""
        temp_dir = tmpdir_factory.mktemp('temp')
        tasks.start_tasks_db(str(temp_dir), request.param)
        yield # this is where the testing happens
        tasks.stop_tasks_db()
        
Here I added _params=['tiny','mongo']_ to the fixture decorator. I added request to the
parameter list of temp_db, and I set db_type to request.param instead of just picking
'tiny' or 'mongo'.
