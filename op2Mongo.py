import pprint
import pandas as pd
import numpy as np
import op2Util as op2u
from pymongo import MongoClient

client = MongoClient()
db = client.betaOphanim2
skeds = db.Skeds
# pprint.pprint(skeds.find_one())
pipeline = [
    {
        '$unwind': {
            'path': '$tasks'
        }
    }, {
        '$match': {
            'tasks.status':'complete',
            'tasks.displayName': 'Bus Dishes in Park'
        }
    }, {
        '$project': {
            '_id':0,
            '_SkedID': 1,
            '_dateCreated': 1,
            'tasks._id': 1,
            'tasks.displayName': 1,
            'tasks.effort': 1,
            'tasks.priority': 1,
            'tasks.status': 1,
            'tasks.startedAt': 1,
            'tasks.completedAt': 1
        }
    }
]
taskList = list(skeds.aggregate(pipeline))
# pprint.pprint(list(skeds.aggregate(pipeline)))
df = pd.DataFrame.from_records(taskList)
# df = pd.DataFrame(list(skeds.find()))
# df1 = df['tasks']
# print(df.head())
# op2u.testPdDict()
dfTaskEffort=op2u.createTaskEffortDF(taskList)
# op2u.getEffortAverage(dfTaskEffort)
# dfl = pd.DataFrame(listTaskEffort)
# op2Columns=['task','effort']
# print(dfl.head())

# createTaskEffortDF
# getEffortAverage
# getSkedEffortAverage
# getSkedEffortAverageByDay
# getSkedEffortAverageForTask
# getDayofWeek