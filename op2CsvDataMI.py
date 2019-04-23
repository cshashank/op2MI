import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/skedData.csv')
# print(df.head())
# df = df.groupby('SkedId').mean()
groupDay = df['Effort'].groupby(df['Day'])
day_effort_mean = groupDay.mean() 
print(day_effort_mean)

day_effort_mean.plot(kind='bar', x='Day', y='effort', color='red')
plt.plot(range(100))
plt.show()

groupTask = df['Effort'].groupby(df['TaskId'])
task_effort_mean = groupTask.mean() 
print(task_effort_mean)

task_effort_mean.plot(kind='bar', x='TaskId', y='effort', color='red')
plt.plot(range(100))
plt.show()

