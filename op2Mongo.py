import pprint
import pandas as pd
import numpy as np
import op2Util as op2u
from pymongo import MongoClient

client = MongoClient()
db = client.betAOphanim2
skeds = db.Skeds
# pprint.pprint(skeds.find_one())
pipeline = [
    {
        '$unwind': {
            'path': '$tasks'
        }
    }, {
        '$match': {
            'tasks.status':'complete'
        }
    }, {
        '$project': {
            '_id':0,
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
listTaskDict=op2u.convertTasksToDict(taskList)
dfl = pd.DataFrame(listTaskDict)
print(dfl.head())