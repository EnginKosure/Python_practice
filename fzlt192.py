import pandas as pd

df = pd.DataFrame({'a': [1, 3, 7, 11, 14, 17]})

bins = [0, 5, 10, 15, 20]

df['binned'] = pd.cut(df['a'], bins=bins)

print(df)
