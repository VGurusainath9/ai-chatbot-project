from pymongo import MongoClient

connection_string = "mongodb+srv://username:password@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client.mydatabase

# List collections in the database
print(db.list_collection_names())
