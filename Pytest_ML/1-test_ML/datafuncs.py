import pandas as pd

import yaml

df = pd.read_csv('data/boston_budget.csv')
print(df.head().to_string())
print()
print(df.columns)
print()

with open('data/metadata_budget.yml', 'r+') as f:
    metadata = yaml.load(f)
print()
print(metadata['columns'])