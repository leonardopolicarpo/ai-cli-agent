from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["neurohub"]

def get_collection(name: str):
  return db[name]
