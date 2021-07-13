import pandas as pd
import numpy as np

df = pd.DataFrame({'a': [1, 3, 7, 11, 14, 17]})

bins = [0, 5, 10, 15, 20]

df['binned'] = pd.cut(df['a'], bins=bins)

print(df)


print(pd.cut(np.array([1, 7, 5, 4, 6, 3]),
             3, labels=["bad", "medium", "good"]))
# [bad, good, medium, medium, good, bad]
# Categories (3, object): [bad < medium < good]
