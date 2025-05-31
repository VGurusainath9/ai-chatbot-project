from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB connection string from .env
connection_string = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(connection_string)
db = client.mydatabase  # Replace with your DB name if different

# List collections in the database
print("Collections:", db.list_collection_names())
