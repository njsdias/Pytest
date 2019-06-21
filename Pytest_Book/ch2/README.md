# Writing Test Functions

In this chapter, you’ll learn how to write test functions in the context of testing a
Python package. If you’re using pytest to test something other than a Python package, most of this chapter still applies.

Eventually, we’ll have a lot of tests. Therefore, you’ll learn how to organize
tests into classes, modules, and directories. I’ll then show you how to use
markers to mark which tests you want to run and discuss how builtin markers
can help you skip tests and mark tests as expecting to fail. Finally, I’ll cover
parametrizing tests, which allows tests to get called with different data.

## Testing a Package

We’ll use the sample project, Tasks, to see how to write test functions for a Python package. Tasks is a
Python package that includes a command-line tool of the same name, tasks.

Following is the file structure for the Tasks project:

![struct_pack_Task](https://user-images.githubusercontent.com/37953610/59927824-397a3a80-9435-11e9-9048-3129ffca265e.JPG)

Files that are of key importance to testing:

- conftest.py

- setup.py

- the various __ init __ .py

**Best practice**: All of the tests are kept in tests and separate from the package source files in src. 

Although _setup.py_ is important for building a distribution out of a package, it’s also crucial for being able to install a package locally so that the package is available for import.

**Functional and unit tests are separated into their own directories.** Organizing test files into multiple
directories allows you to easily run a subset of tests. Separate functional
and unit tests:

- functional tests should only break if we are intentionally changing functionality of the system

- unit tests could break during a refactoring or an implementation change.

Folder with **__init__ .py** file tells Python
that the directory is a package. It also acts as the main interface to the
package when someone uses import tasks. It also acts as the main interface to the
package when someone uses import tasks. It contains code to import specific
functions from api.py so that cli.py and our test files can access package functionality
like _tasks.add()_ instead of having to do _tasks.api.add()_.

The **tests/func/__init__.py** and **tests/unit/__init__.py** files **are empty**. They tell pytest to
**go up one directory to look for the root of the test directory and to look for
the pytest.ini file.** The pytest.ini file is optional. It contains project-wide pytest configuration. There
should be at most only one of these in your project. It can contain directives
that change the behavior of pytest, such as setting up a list of options that
will always be used. 

The **conftest.py** file is also optional. It is considered by pytest as a “local plugin”
and can contain hook functions and fixtures. **Hook functions** are a way to
insert code into part of the pytest execution process to alter how pytest works.
**Fixtures** are setup and teardown functions that run before and after test
functions, and can be used to represent resources and data used by the
tests. Hook functions and fixtures that are used by tests in multiple subdirectories should be contained in tests/conftest.py. You
can have multiple conftest.py files; for example, you can have one at tests and one for each subdirectory under tests.

The _test_task.py_ file has this import statement:

    from tasks import Task

The best way to allow the tests to be able to _import tasks_ or _from tasks import something_
is to install tasks locally using pip. **This is possible because there’s a setup.py
file present to direct pip.** Install tasks either by running _pip install_ . or _pip install -e_ . from the tasks_proj directory.
Or you can run _pip install -e tasks_proj_ from one directory up:

    cd /path/to/code
    pip install ./tasks_proj/
    pip install --no-cache-dir ./tasks_proj/
    Processing ./tasks_proj

## Expecting Exceptions

Exceptions may be raised in a few places in the Tasks API. Let’s take a quick
peek at the functions found in tasks/api.py:

    def add(task): # type: (Task) -> int
    def get(task_id): # type: (int) -> Task
    def list_tasks(owner=None): # type: (str|None) -> list of Task
    def count(): # type: (None) -> int
    def update(task_id, task): # type: (int, Task) -> None
    def delete(task_id): # type: (int) -> None
    def delete_all(): # type: () -> None
    def unique_id(): # type: () -> int
    def start_tasks_db(db_path, db_type): # type: (str, str) -> None
    def stop_tasks_db(): # type: () -> None
    
There’s an agreement between the CLI code in cli.py and the API code in api.py
as to what types will be sent to the API functions. These API calls are a place
where I’d expect exceptions to be raised if the type is wrong.

## Marking Test Functions

pytest provides a cool mechanism to let you put markers on test functions.
A test can have more than one marker, and a marker can be on multiple
tests.

Markers make sense after you see them in action. Let’s say we want to run
a subset of our tests as a quick “smoke test” to get a sense for whether or not
there is some major break in the system. Smoke tests are by convention not
all-inclusive, thorough test suites, but a select subset that can be run
quickly and give a developer a decent idea of the health of all parts of the
system.

To add a smoke test suite to the Tasks project, we can add **@mark.pytest.smoke**
to some of the tests. 


## Skipping Tests

Marking a test to be skipped is as simple as adding **@pytest.mark.skip()** just above
the test function.

    @pytest.mark.skip(reason='misunderstood the API')
    def test_unique_id_1():
        """Calling unique_id() twice should return different numbers."""
        id_1 = tasks.unique_id()
        id_2 = tasks.unique_id()
        assert id_1 != id_2

Now, let’s say that for some reason we decide the first test should be valid
also, and we intend to make that work in version 0.2.0 of the package. We
can leave the test in place and use **skipif** instead:

ch2/tasks_proj/tests/func/test_unique_id_3.py

    @pytest.mark.skipif(tasks.__version__ < '0.2.0', reason='not supported until version 0.2.0')
    def test_unique_id_1():
        """Calling unique_id() twice should return different numbers."""
        id_1 = tasks.unique_id()
        id_2 = tasks.unique_id()
        assert id_1 != id_2
        
The expression we pass into skipif() can be any valid Python expression. In this
case, we’re checking the package version.
We included reasons in both skip and skipif. It’s not required in skip, but it is
required in skipif. I like to include a reason for every skip, skipif, or xfail.

The x is for XFAIL, which means “expected to fail.” The capital X is for XPASS or
“expected to fail but passed.”

    pytest -v test_unique_id_4.py
    
You can configure pytest to report the tests that pass but were marked with
xfail to be reported as FAIL. This is done in a **pytest.ini** file: 

    [pytest]
    xfail_strict=true
    
## Running a subset of tests

- All inside of a folder

      pytest -v tests/func --tb=no
    
- All inside a file.py

      pytest tests/func/test_add.py
    
- A specific test inside a file

      pytest -v tests/func/test_add.py::test_add_returns_valid_id

- A single test class. In this case we defined a class named TestUpdate

      pytest -v tests/func/test_api_exceptions.py::TestUpdate

- A Single Test Method of a Test Class. In this case we are running the test test_bad_id that is inside of TestUpdate class

      pytest -v tests/func/test_api_exceptions.py::TestUpdate::test_bad_id
    
- A Set of Tests Based on Test Name: using the option -k enables you to pass in an expression to run tests that have
certain names specified by the expression as a substring of the test name.
You can use and, or, and not in your expression to create complex expressions. For example, we can run all of the functions that have _raises in their name:

    pytest -v -k _raises
    
  - We can use and and not to get rid of the test_delete_raises() from the session:
    
        pytest -v -k "_raises and not delete"    
