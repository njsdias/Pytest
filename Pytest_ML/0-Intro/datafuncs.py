import numpy as np

def increment(x):
    return x + 1

# min_max sclaer should take in a numpy array and scale all of the values to be between 0 and 1.
# The min value should be 0 and the max value should be 1.
def min_max_scaler(x):
    """
    Returns a numpy array with all of the original values sclaed between 0 and 1
    Assumes the data are a numpy array
    """

   # if (hasattr(x, __iter__) and not isinstance(x,np.array)):
   #     x = np.array(x)

    # assert isinstance(x, np.array) , "x should be a numpy array"
    # assert len(set(x)) > 1, "x should have more than 1 unique value"

    unique_vals = np.unique(x)  # checks how many unique values
    if len(unique_vals) == 1 and isinstance(x, list):
        return np.array([0.5] * len(x))
    else:
        return ((x - x.min()) / (x.max() - x.min()))

"""
Implement a function that clips data to be within a particular range.

- have the function signature clip(data, lower, upper), where:
    - data is a numpy array-like data structure.
    - lower is the lower-bound value.
    - upper is the upper-bound value.
- set any data points lower than lower to the value of lower
- set any data points greater than upper to the value of upper

"""
def clips(data,lower,upper):
    data[data < lower] = lower
    data[data > upper] = upper
    return data
