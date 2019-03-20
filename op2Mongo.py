import pprint

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
            'tasks.displayName': 'Replenish Item'
        }
    }, {
        '$project': {
            'status': 1,
            'tasks.effort': 1,
            'tasks.priority': 1
        }
    }
]
task_effort = list(skeds.aggregate(pipeline))
# pprint.pprint(list(skeds.aggregate(pipeline)))

for tef in skeds.aggregate(pipeline):
    pprint.pprint(tef)
    task = tef['tasks']
    pprint.pprint(task['effort'])