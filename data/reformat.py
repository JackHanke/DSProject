import pandas as pd
df = pd.read_csv('./data.csv')
df.to_parquet('./data.parquet')
df = pd.read_csv('./labels.csv')
df.to_parquet('./labels.parquet')