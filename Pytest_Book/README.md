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

