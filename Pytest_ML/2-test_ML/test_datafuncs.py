
import pandas as pd
from pandas_summary import DataFrameSummary

#This function is used to check if the data are completed
def check_data_completeness(df):
    df_summary = DataFrameSummary(df).summary()
    for col in df_summary.columns:
        assert df_summary.loc['missing',col] == 0 , f'{col} has missing values'

def test_boston_ei():
    df = pd.read_csv('data/boston_ei.csv')
    check_data_completeness(df)