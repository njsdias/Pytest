"""
Let's modify this test with a "property-based" test. In this case, we may choose to test it with a bunch of
 integers sampled using Hypothesis' strategies module.

"""
# pip install hypotesis

from hypothesis import given, assume
from hypothesis import strategies as st
import datafuncs as dfn

"""
hypothesis.strategies.integers(min_value=None, max_value=None)[source]
Returns a strategy which generates integers; in Python 2 these may be ints or longs.

If min_value is not None then all values will be >= min_value. 
If max_value is not None then all values will be <= max_value

Examples from this strategy will shrink towards zero, and negative values will also shrink towards positive 
(i.e. -n may be replaced by +n).
"""


@given(st.integers())  # We are going to test a wide range of integers.
def test_increment(x):
    assert dfn.increment(x) - 1 == x

@given(st.integers(),st.integers(),st.integers())
def test_eq_roots(a, b, c):
    coefficients = (a, b, c)
    discriminant = b**2 - 4*a*c
    assume(discriminant >= 0)
    assume(a > 0)
    r1, r2 = dfn.eq_roots(coefficients)
    assert r1 >= r2