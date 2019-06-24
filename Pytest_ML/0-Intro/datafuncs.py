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

    return (x - x.min()) / (x.max()-x.min())
