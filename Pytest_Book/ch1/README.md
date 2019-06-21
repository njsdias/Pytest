# Task project

Another great use of software tests is to test your assumptions about how
the software under test works, which can include testing your understanding
of third-party modules and packages, and even builtin Python data structures.
The **Tasks project** uses a structure called Task, which is based on the _namedtuple_
factory method, which is part of the standard library. The Task structure
**is used as a data structure to pass information between the UI and the API**.

Here’s Task:

    from collections import namedtuple
    Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])

## Name Convention for the tests
The part of pytest execution where pytest goes off and finds which tests to
run is called **test discovery**. pytest was able to find all the tests we wanted it
to run because we named them according to the pytest naming conventions.
Here’s a brief overview of **the naming conventions** to keep your test code discoverable
by pytest:

• Test files should be named test_<something>.py or <something>_test.py.
    
• Test methods and functions should be named test_<something>.
• Test classes should be named Test<Something>.
    
## Output of tests

Since our test files and functions start with test_, we’re good

The outcome of a test is the primary way the person running a test or looking
at the results understands what happened in the test run. In pytest, test
functions may have several different outcomes, not just pass or fail.
Here are the possible outcomes of a test function:

• PASSED (.): The test ran successfully.

• FAILED (F): The test did not run successfully (or XPASS + strict).

• SKIPPED (s): The test was skipped. You can tell pytest to skip a test by
using either the @pytest.mark.skip() or pytest.mark.skipif() decorators.

• xfail (x): The test was not supposed to pass, ran, and failed. You can tell
pytest that a test is expected to fail by using the @pytest.mark.xfail() decorator

• XPASS (X): The test was not supposed to pass, ran, and passed.

• ERROR (E): An exception happened outside of the test function, in either
a fixture.

## Options of pytest

        pytest --help

-k EXPRESSION only run tests/classes which match the given
substring expression.

   - Example: -k 'test_method or test_other' matches all test functions and classes whose name contains 'test_method' or 'test_other'.
   
-m MARKEXPR only run tests matching given mark expression.

   - Example: -m 'mark1 and not mark2'.
   
-x, --exitfirst exit instantly on first error or failed test.

--maxfail=num exit after first num failures or errors.

--capture=method per-test capturing method: one of fd|sys|no.

-s shortcut for --capture=no.

--lf, --last-failed rerun only the tests that failed last time (or all if none failed)

--ff, --failed-first run all tests but run the last failures first.

-v, --verbose increase verbosity.

-q, --quiet decrease verbosity.

-l, --showlocals show locals in tracebacks (disabled by default).

--tb=style traceback print mode (auto/long/short/line/native/no).

--durations=N show N slowest setup/test durations (N=0 for all).

--collect-only only collect tests, don't execute them.

--version display pytest lib version and import information.

-h, --help show help message and configuration info
