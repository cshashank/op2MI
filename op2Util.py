from dateutil import parser
import time
import datetime
import pandas as pd
import numpy as np
from datetime import date
import pymongo

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

def convertTasksToDict(taskList):
    print('in convert task to dict')
    listTaskEffort=[]
    for task in taskList:
        listTasks = task['tasks']
        startedDateTime = listTasks['startedAt']
        endDateTime = listTasks['completedAt']
        timeTaken = pd.to_datetime(endDateTime)-pd.to_datetime(startedDateTime)
        rEffort = timeTaken.round
        # listTaskDict.append['timeTake':timeTaken]
        listTaskEffort.append([listTasks['_id'],(timeTaken.total_seconds())])
    df_t = pd.DataFrame(listTaskEffort)
    print(df_t.dtypes)
    df_t.columns= ['task', 'effort']
    decimals=2
    # df_t.effort=df_t.effort.apply(lambda x: round(x,decimals))
    df_t.effort=df_t.effort.round(decimals)
    print(df_t.head())
    # print(listTaskEffort)
    return listTaskEffort
