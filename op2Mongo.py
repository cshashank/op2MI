import pprint

from pymongo import MongoClient

client = MongoClient()
db = client.betAOphanim2
skeds = db.Skeds
pprint.pprint(skeds.find_one())
query =[
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