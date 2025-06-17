from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB_NAME", "ai-cli-agent")
DEFAULT_COLLECTION = os.getenv("MONGO_COLLECTION_NAME", "interactions")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def get_collection(name: str = DEFAULT_COLLECTION):
    return db[name]
