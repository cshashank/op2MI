from dateutil import parser
import time
import datetime
import pandas
from datetime import date

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
