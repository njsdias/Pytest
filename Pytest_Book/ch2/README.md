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










