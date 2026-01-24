import pandas as pd

df = pd.read_csv('data/strong_workouts.csv')
print(df.head(10))

print(df.shape)

print(df.columns)

print(df.describe())