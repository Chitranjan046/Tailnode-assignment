import requests
import pymongo
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
MONGODB_URL = os.getenv("MONGODB_URL")
API_KEY = os.getenv("API_KEY")

# Init PyMongo
client = pymongo.MongoClient(MONGODB_URL)
db = client.tailnode
user_collection = db.users

# Insert User Data into Database
r = requests.get("https://dummyapi.io/data/v1/user", headers={"app-id": API_KEY}).json()
user_data = r['data']

result = user_collection.insert_many(user_data)
print("User Data inserted successfully", result.inserted_ids)
