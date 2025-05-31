from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Mongo URI from environment variables
connection_string = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(connection_string)
db = client["mydatabase"]  # Replace with your actual database name

# List collections
print("Collections in the database:")
print(db.list_collection_names())
