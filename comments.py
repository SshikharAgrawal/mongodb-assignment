from pymongo import MongoClient
import json
import subprocess
import pprint
from datetime import datetime
client = MongoClient('mongodb://localhost:27017/')

db=client['myDB']
# for doc in db['users'].find():
#     # print(doc)cursor = db['collection'].find({})

# cursor = db['comments'].find({})
# for document in cursor: 
#     print(document.keys())  # print all fields of this document. 

def query1():
    comments=db['comments']
    res1=comments.aggregate([{"$group":{"_id":"$name","count":{"$sum":1}}},{"$sort":{"count":-1}},{'$limit':10}])
    for i in res1:
        print(i)

def query2():
    comments=db['comments']
    res1=comments.aggregate([{"$group":{"_id":"$movie_id","count":{"$sum":1}}},{"$sort":{"count":-1}},{"$limit":10}])
    for i in res1:
        print(i)

def query3():
    col=db['comments']
    documents = col.find({"date": {"$type": "long"}})
    for doc in documents:
        timestamp = int(doc["date"]) / 1000  # Convert to seconds
        date = datetime.fromtimestamp(timestamp)
        col.update_one({"_id": doc["_id"]}, {"$mul": {"date": 0}, "$set": {"date": date}})   
    res1=col.aggregate([{"$project" : {"month":{"$month":"$date"}}},{"$group":{"_id":"$month","count":{"$sum":1}}}]) 
    for document in res1:
        print(document)
