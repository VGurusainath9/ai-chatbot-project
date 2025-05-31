from pymongo import MongoClient

# Use URL-encoded password (%40 for '@')
uri = "mongodb+srv://vgurusainaths:Guru9%402001@clustera.bw2gutg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"

client = MongoClient(uri)

# Access your database (replace 'test' with your DB name)
db = client.test

# Print collections to test connection
print(db.list_collection_names())
