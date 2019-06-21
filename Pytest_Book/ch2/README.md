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

- __ init __ .py
