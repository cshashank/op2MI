import pprint
import pandas as pd
import numpy as np
import op2Util as op2u

df = pd.read_csv('data/skedData.csv')
# print(df.head())
# df = df.groupby('SkedId').mean()
group = df['Effort'].groupby([df['SkedId'],df['Day']])
print(group.mean())
