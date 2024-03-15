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
