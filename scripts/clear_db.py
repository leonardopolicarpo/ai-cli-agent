from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client[os.getenv("MONGO_DB_NAME", "neurohub")]

db["interactions"].delete_many({})

print("Banco limpo com sucesso.")
