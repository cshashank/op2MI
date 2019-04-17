from dateutil import parser
import time
import datetime
import pandas as pd
import numpy as np
from datetime import date
import pymongo
import matplotlib.pyplot as plt

def getDate():
    from datetime import datetime
    pprint.pprint('skc test')

def getDate(strDate):
    dt = parser.parse(strDate)
    return dt

def printMongoCursor(skeds):
    #skeds = db.Skeds
    #The skeds collection from Ophanim database
    for tef in skeds.aggregate(pipeline):
        # pprint.pprint(tef)
        task = tef['tasks']
        # completedDate = task['completedAt']
        dtCompletedAt = getDate(task['completedAt'])
        dtStartedAt = getDate(task['startedAt'])

        # pprint.pprint((dtCompletedAt-dtStartedAt))

        # print(task['completedAt']+','+task['startedAt']+','+str((dtCompletedAt-dtStartedAt)))

def testPdDict():
    temp = [{'points': 50, 'time': '5:00', 'year': 2010},
            {'points': 25, 'time': '6:00', 'month': "february"},
            {'points': 90, 'time': '9:00', 'month': 'january'},
            {'points_h1': 20, 'month': 'june'}]
    df1 = pd.DataFrame(temp)
    print(df1.head())

def createTaskEffortDF(taskList):
    print('in convert task to dict')
    listTaskEffort=[]
    for task in taskList:
        skedId = task['_SkedID']
        skedDate = task['_dateCreated']
        listTasks = task['tasks']
        startedDateTime = listTasks['startedAt']
        endDateTime = listTasks['completedAt']
        timeTaken = pd.to_datetime(endDateTime)-pd.to_datetime(startedDateTime)
        rEffort = timeTaken.round
        # listTaskDict.append['timeTake':timeTaken]
        listTaskEffort.append([skedId,skedDate.strftime("%a"),listTasks['displayName'],(timeTaken.total_seconds())/60])
    df_t = pd.DataFrame(listTaskEffort)
    # print(df_t.dtypes)
    df_t.columns = ['skedId','day','task', 'effort']
    decimals = 2
    # df_t.effort=df_t.effort.apply(lambda x: round(x,decimals))
    df_t.effort = df_t.effort.round(decimals)
    # print(df_t.head())
    # getSkedEffortAverageByDay(df_t)
    # getSkedEffortAverage(df_t)
    # getSkedEffortAverageForTask(df_t, "Arrange Bar Stools in Bar Area")
    # getDayOfWeek(skedDate)
    getEffortAverage(df_t)
    # print(listTaskEffort)
    return df_t

def getEffortAverage(effortsDf):
    decimals = 2
    df = effortsDf.groupby('task').mean()
    df.effort = df.effort.round(decimals)
    print('^^^^^^^^^^^^^^')
    df_effort = effortsDf
    del df_effort['day']
    del df_effort['task']
    print(df_effort.head())

    # print(df_plot.head())
    # print(df_plot.count)
    # df_plot=df_plot.skedId
    # print(df_plot.head())

    df.plot(kind='bar', x='skedId', y='effort', color='red')
    plt.plot(range(100))
    plt.show()

def getSkedEffortAverage(effortsDf):
    decimals = 2
    # print(arrangeDf.head())
    df = effortsDf.groupby(['skedId','task']).mean()
    df = arrangeDf.groupby(['skedId']).mean()
    df.effort = df.effort.round(decimals)
    print(df.head(20))
    # print(df.count)

def getSkedEffortAverageByDay(effortsDf):
    decimals = 2
    # print(arrangeDf.head())
    df = effortsDf.groupby(['day','skedId','task']).mean()
    # df = arrangeDf.groupby(['skedId']).mean()
    print('@@@@@@@@@@@@@@@@@@@')
    df.effort = df.effort.round(2)
    print(df.count())
    print(df)

def getSkedEffortAverageForTask(effortsDf,taskName):
    decimals = 2
    # arrangeFilterDf = effortsDf['task'] == "Arrange Bar Stools in Bar Area"
    arrangeFilterDf = effortsDf['task'] == taskName
    arrangeDf = effortsDf[arrangeFilterDf]
    # print(arrangeDf.head())
    # df = effortsDf.groupby(['skedId','task']).mean()
    df = arrangeDf.groupby(['skedId']).mean()
    df.effort = df.effort.round(decimals)
    print('task name '+taskName)
    print(df.head(20))
    # print(df.count)

def getDayOfWeek(skedDate):
    print(skedDate.year)
    print(skedDate.strftime("%a"))