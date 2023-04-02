from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db=client['myDB']

def query11(n):
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            {
                "$match":{"imdb.rating":{"$ne":""}}
            },
            {
                "$sort":{"imdb.rating":-1}   
            }
        ]
    )
    cnt=0
    for i in res1:
        if(cnt<n):
            cnt=cnt+1
            print(i)
 
def query12(year):
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            {
                "$match":{"imdb.rating":{"$ne":""},"year":year}
            },
            {
                "$group":{"_id":"$year",'maxrating':{"$max":'$imdb.rating'}}
            }
        ]
    )
    for i in res1:
        print(i)

def query13():
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            {
                "$match":{"imdb.rating":{"$ne":""},"imdb.votes":{"$gt":10000}}
            },
            {
                "$group":{"_id":"","maxrating":{"$max":'$imdb.rating'}}
            }
        ]
    )
    for i in res1:
        print(i)

def query14(pattern):
        movies=db['movies']
        res = movies.find(
            {"title": {"$regex": pattern}},
            {"title":1, "tomatoes.viewer":1}
            ).sort("tomatoes.viewer.rating",-1).limit(10)
        

def query21():
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            {
                "$unwind":"$directors"
            },
            {
                "$group":{"_id":"$directors","count":{"$sum":1}}
            },
            # {
            #     "$match": {"_id": "Woody Allen"}
            # }
            {
                "$sort":{"count": -1}
            }
        ]
    )
    for i in res1:
        print(i)

def query22(year):
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            {
                "$match":{"year":year}
            },
            {
                "$unwind":"$directors"
            },
            {
                "$group":{"_id":"$directors","count":{"$sum":1}}
            },
            {
                "$sort":{"count":-1}
            },{
                "$limit":1
            }
          
        ]
    )
    for i in res1:
        print(i)

def query23(genre):
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            
            {
                "$unwind":"$genres"
            },
            {
                "$unwind":"$directors"
            },
            {
                "$match":{"genres":genre}
            },
            {
                "$group":{"_id":"$directors","count":{"$sum":1}}
            },
            {
                "$sort":{"count":-1}
            },
            {
                "$limit":1
            }
          
        ]
    )
    for i in res1:
        print(i)
    
def query31(n):
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            
            {
                "$unwind":"$cast"
            },
            {
                "$group":{"_id":"$cast","count":{"$sum":1}}
            },
            {
                "$sort":{"count":-1}
            },
            {
                "$limit":n
            }
          
        ]
    )
    for i in res1:
        print(i)
def query32(year,n):
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            
            {
                "$unwind":"$cast"
            },
            {
                "$match":{"year":year}
            },
            {
                "$group":{"_id":"$cast","count":{"$sum":1}}
            },
            {
                "$sort":{"count":-1}
            },
            {
                "$limit":n
            }
          
        ]
    )
    for i in res1:
        print(i)

def query33(genre,n):
    movies=db['movies']
#  ,{"$match":{"$rating":{"$ne":" "}}},{"$sort":{"imdb":-1}}
    res1=movies.aggregate(
        [
            
            {
                "$unwind":"$genres"
            },
            {
                "$unwind":"$cast"
            },
            {
                "$match":{"genres":genre}
            },
            {
                "$group":{"_id":"$cast","count":{"$sum":1}}
            },
            {
                "$sort":{"count":-1}
            },
            {
                "$limit":n
            }
          
        ]
    )
    for i in res1:
        print(i)

def query41():
        movies=db['movies']
        genres = movies.aggregate(
            [
            {"$unwind":"$genres"},
              {"$group":{"_id":"$genres"}}
            ]
        )
        for i in genres:
            genre = i['_id']
            res = movies.aggregate(
                [   
                    {"$match": {"genres":genre, "imdb.rating": {"$ne":""} }},
                    {"$sort": {"imdb.rating":-1}}, 
                    {"$limit":4}
                ])
            for i in res:
                print(i)
