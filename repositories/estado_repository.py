from pymongo import MongoClient
from repositories.config import uri

client = MongoClient(uri)
db = client.CodigosPostales
collection = db["Estados"]

def get_estados():
    estados = collection.find()
    # for estado in estados:
    #     print(estado)
    return estados
