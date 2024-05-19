import argparse
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://userweb16:example@cluster0.q1gz4ma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.web16

parser = argparse.ArgumentParser(description='Server Cats Interprise')
parser.add_argument('--action', help='create, update, read, delete')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age', type=int)
parser.add_argument('--features', nargs='+')

args = vars(parser.parse_args())

action = args.get('action')
pk = args.get('id')
name = args.get('name')
age = args.get('age')
features = args.get('features')

def find():
    return db.cats.find({},{"_id":0})

def create(name, age, features):
    result = db.cats.insert_one({
        "name": name, 
        "age": age, 
        "features": features
        })
    return {"inserted_id": str(result.inserted_id)}

def update(pk, name, age, features):
    result = db.cats.update_one(
        {"_id": ObjectId(pk)},
        {"$set": {"name": name, "age": age, "features": features}}
    )
    return {"matched_count": result.matched_count, "modified_count": result.modified_count}

def delete(pk):
    result = db.cats.delete_one({"_id": ObjectId(pk)})
    return {"deleted_count": result.deleted_count}

def main():
    match action: 
        case 'create':
            if name and age is not None and features:
                r = create(name, age, features)
                print(r)
            else:
                print("Name, age, and features are required for creating a new cat.")
        
        case 'read':
            r = find()
            print([e for e in r])
        
        case 'update':
            if pk and name and age is not None and features:
                r = update(pk, name, age, features)
                print(r)
            else:
                print("ID, name, age, and features are required for updating a cat.")

        case 'delete':
            if pk:
                r = delete(pk)
                print(r)
            else:
                print("ID is required for deleting a cat.")
        
        case _:
            print('Unknown command')

if __name__ == "__main__":
    main()
