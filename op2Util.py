from dateutil import parser
import time
import datetime
import pandas as pd
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
    listTaskDict=[]
    for task in taskList:
        startedDateTime = task['startedAt']
        endDateTime = task['completedAt']
        timeTaken = endDateTime-startedDateTime
        print(timeTaken)
        listTaskDict.append(task['tasks'])

    # print(listTaskDict)
    return listTaskDict
