from pymongo import MongoClient
from repositories.config import uri

client = MongoClient(uri)
db = client["Utilidades"]
collection = db["NumerosBancarios"]

def get_all():
    inventory = collection.find()
    return inventory