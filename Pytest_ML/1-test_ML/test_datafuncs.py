

# Here is where you write your test functions

# We want write a test function to check the schema of a dataframe

import pandas as pd
import yaml


def check_schema(df, metacolumns):
    for col in df.columns:
        assert col in metacolumns, f'"{col} not in metadata column spec"'

def test_budget_schemas():
    with open('data/metadata_budget.yml', 'r+') as f:
        metadata = yaml.load(f)
    columns = metadata['columns']
    df = pd.read_csv('data/boston_budget.csv')
    check_schema(df, columns)

