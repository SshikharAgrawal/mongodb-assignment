from pymongo import MongoClient
import json
import subprocess
client = MongoClient('mongodb://localhost:27017/')

db=client['myDB']

subprocess.call(["mongoimport","--db","myDB","--collection","sessions","--file","sessions.json"])
subprocess.call(["mongoimport","--db","myDB","--collection","threaters","--file","theaters.json"])
subprocess.call(["mongoimport","--db","myDB","--collection","users","--file","users.json"])
subprocess.call(["mongoimport","--db","myDB","--collection","comments","--file","comments.json"])


