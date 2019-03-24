import pprint
import pandas as pd
from op2Util import getDate
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
            'tasks.effort': 1,
            'tasks.priority': 1,
            'tasks.status': 1,
            'tasks.startedAt': 1,
            'tasks.completedAt': 1
        }
    }
]
task_effort = list(skeds.aggregate(pipeline))
# pprint.pprint(list(skeds.aggregate(pipeline)))
df = pd.DataFrame(skeds.aggregate(pipeline))
print(df.head()['tasks'])
