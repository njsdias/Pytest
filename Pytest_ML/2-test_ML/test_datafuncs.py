import pytest
import pandas as pd

from pandas_summary import DataFrameSummary



#This function is used to check if the data are completed
def check_data_completeness(df):
    df_summary = DataFrameSummary(df).summary()
    for col in df_summary.columns:
        assert df_summary.loc['missing',col] == 0 , f'{col} has missing values'

@pytest.mark.bostfirst
def test_boston_ei():
    df = pd.read_csv('data/boston_ei.csv')
    check_data_completeness(df)


"""
Exercise: Test for value correctness.
In the Economic Indicators dataset, there are four "rate" columns: ['labor_force_part_rate', 'hotel_occup_rate', 
'hotel_avg_daily_rate', 'unemp_rate'], which must have values between 0 and 1.

Add a utility function to test_datafuncs.py, check_data_range(data, lower=0, upper=1), which checks the range of 
the data such that:

data is a list-like object.
data <= upper
data >= lower
upper and lower have default values of 1 and 0 respectively.
Then, add to the test_boston_ei() function tests for each of these four columns, using the check_data_range() function.

"""

def check_data_range(data, lower=0, upper=1):
    assert min(data) >= lower, f"minimum value less than {lower}"    # check if column have values >= zero
    assert max(data) <= upper, f"maximum value greater then {upper}" # check if colunm have values <= one

def test_boston_ei():
    df = pd.read_csv('data/boston_ei.csv')
    check_data_completeness(df)

    zero_one_cols = ['labor_force_part_rate', 'hotel_occup_rate',
                     'hotel_avg_daily_rate', 'unemp_rate']
    for col in zero_one_cols:
        check_data_range(df['labor_force_part_rate'])