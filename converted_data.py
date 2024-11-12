import pandas as pd

data_df = pd.read_csv('data.csv')
labels_df = pd.read_csv('labels.csv')

data_df.to_parquet('data.parquet', engine='pyarrow')  
labels_df.to_parquet('labels.parquet', engine='pyarrow')

print("CSV files successfully converted to Parquet format.")
