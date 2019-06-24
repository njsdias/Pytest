
# This is only for exploratory data

import pandas as pd
import seaborn as sns
import matplotlib

sns.set_style('white')
#%matplotlib inline

df = pd.read_csv('data/boston_ei-corrupt.csv')
print(df.head().to_string())

# We can do the same using pandas-summary.
from pandas_summary import DataFrameSummary

dfs = DataFrameSummary(df)
print(dfs.summary().columns)