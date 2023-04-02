from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db=client['myDB']


def query11():
    theaters=db["threaters"]
    res1=theaters.aggregate([
        {
        "$group":{"_id":"$location.address.city","count":{"$sum":1}}
        },
        {
        "$sort":{"count":-1}
        },{
        "$limit":10
        }
    ])
    for i in res1:
        print(i)

def query12():
    theaters=db["threaters"]
    res = theaters.aggregate([
        {"$geoNear": {"near":{ "type": "Point", "coordinates": [ -73.99279 , 40.719296 ] }, 
            "distanceField":"dist.calculated", 
            "maxDistance":10000, 
            "includeLocs": "dist.location", 
            "spherical":"true"
        }},
        {"$limit":6}
    ])


query11()
query12()
