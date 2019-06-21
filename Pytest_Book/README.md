# Pytest

The N-output.txt have the command line used to run the tests and the output of those tests. 

Here are a few of the reasons pytest stands out above many other test
frameworks:

• Simple tests are simple to write in pytest.

• Complex tests are still simple to write.

• Tests are easy to read.

• Tests are easy to read. (So important it’s listed twice.)

• You can get started in seconds.

• You use assert to fail a test, not things like _self.assertEqual()_ or _self.assertLessThan()_. Just _assert_.

• You can use pytest to run tests written for unittest or nose.

**Test Strategy**

While pytest is useful for unit testing, integration testing, system or end-toend
testing, and functional testing, the strategy for testing the Tasks project
focuses primarily on subcutaneous functional testing. Following are some
helpful definitions:

• **Unit test:** A test that checks a small bit of code, like a function or a class,
in isolation of the rest of the system. I consider the tests in Chapter 1,
Getting Started with pytest, on page 1, to be unit tests run against the
Tasks data structure.

• **Integration test:** A test that checks a larger bit of the code, maybe several
classes, or a subsystem. Mostly it’s a label used for some test larger than
a unit test, but smaller than a system test.

• **System test (end-to-end):** A test that checks all of the system under test
in an environment as close to the end-user environment as possible.

• **Functional test:** A test that checks a single bit of functionality of a system.
A test that checks how well we add or delete or update a task item in
Tasks is a functional test.

• **Subcutaneous test:** A test that doesn’t run against the final end-user
interface, but against an interface just below the surface. Since most of
the tests in this book test against the API layer—not the CLI—they qualify
as subcutaneous tests.

## Task project

Another great use of software tests is to test your assumptions about how
the software under test works, which can include testing your understanding
of third-party modules and packages, and even builtin Python data structures.
The **Tasks project** uses a structure called Task, which is based on the _namedtuple_
factory method, which is part of the standard library. The Task structure
**is used as a data structure to pass information between the UI and the API**.

Here’s Task:

    from collections import namedtuple
    Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])


The part of pytest execution where pytest goes off and finds which tests to
run is called **test discovery**. pytest was able to find all the tests we wanted it
to run because we named them according to the pytest naming conventions.
Here’s a brief overview of **the naming conventions** to keep your test code discoverable
by pytest:

• Test files should be named test_<something>.py or <something>_test.py.
    
• Test methods and functions should be named test_<something>.
• Test classes should be named Test<Something>.
    
Since our test files and functions start with test_, we’re good

