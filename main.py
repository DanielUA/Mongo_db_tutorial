from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://userweb16:example@cluster0.q1gz4ma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.web16
# Send a ping to confirm a successful connection
try:
    db.cats.insert_many([
    {
        "name": 'Boris',
        "age": 12,
        "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
    },
    {
        "name": 'Murzik',
        "age": 1,
        "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
    },
])

except Exception as e:
    print(e)



