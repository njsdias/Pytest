
import pytest
import datafuncs as dfn
import numpy as np

def test_incement():
    #assert dfn.increment(2) != 3    # this will give a error because 2 +1 = 3 and not !=3 as expected
    assert dfn.increment(2) == 3    # this not give us an error because 2 +1 == 3 as expected

# min_max sclaer should take in a numpy array and scale all of the values to be between 0 and 1.
# The min value should be 0 and the max value should be 1.
def test_min_max_scaler():
    arr = np.array([1, 2, 3])  # set up the test with necessary variables.
    tfm = dfn.min_max_scaler(arr)  # collect the result into a variable
    # Correctness tests
    assert np.allclose(tfm, np.array([0, 0.5, 1]))  # assertion statements
    assert tfm.min() == 0
    assert tfm.max() == 1

    all_same = [1, 1]
    tfm_same = dfn.min_max_scaler(all_same)
    assert np.allclose(tfm_same, 0.5)

    with pytest.raises(AssertionError):
        dfn.min_max_scaler(2)                       # test if the array is a list
        dfn.min_max_scaler([])                      # test if the array in empty
        dfn.min_max_scale([15])                     # test if the array have only one element