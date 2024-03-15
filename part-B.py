import pymongo
import requests
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Access the environment variables
MONGODB_URL = os.getenv("MONGODB_URL")

# Create function to connect to MongoDB Atlas and get a reference to the collection using pymongo lib.
def database_collection():
    client = pymongo.MongoClient(MONGODB_URL)
    db = client.tailnode  # Use your database name
    collection = db.books
    return collection

