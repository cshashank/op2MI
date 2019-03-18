import pprint

from pymongo import MongoClient

client = MongoClient()
db = client.betAOphanim2
inventory = db.Inventory
pprint.pprint(inventory.find_one())
