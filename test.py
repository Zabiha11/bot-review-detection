import pandas as pd

df = pd.read_parquet("data/processed/train.parquet")

print(df.groupby("label")["rating"].mean())

print(df.groupby("label")["burst_score"].mean())