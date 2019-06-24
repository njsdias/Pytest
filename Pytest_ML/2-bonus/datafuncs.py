import math
"""

Property-based testing
From the Hypothesis docs:

It works by letting you write tests that assert that something should be true for every case,
not just the ones you happen to think of.

Think of a normal unit test as being something like the following:

Set up some data.
Perform some operations on the data.
Assert something about the result.
Hypothesis lets you write tests which instead look like this:

For all data matching some specification.
Perform some operations on the data.
Assert something about the result.
This is often called property based testing, and was popularised by the Haskell library Quickcheck.

"""

def increment(x):
    return x + 1

def eq_roots(coefficients):
    a, b, c = coefficients
    discriminant = b**2 - 4*a*c
    assert discriminant >= 0
    assert a > 0
    root1 = (-a + math.sqrt(discriminant))/(2*a)
    root2 = (-a - math.sqrt(discriminant))/(2*a)
    return root1, root2