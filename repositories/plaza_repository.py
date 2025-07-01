from pymongo import MongoClient
from repositories.config import uri

client = MongoClient(uri)
db = client.Utilidades
collection = db["PlazasParaClabe"]


def get_random_plaza():
    plaza = collection.aggregate([{"$sample": {"size": 1}}]).next()

    return plaza


def get_all():
    inventory = collection.find()

    return inventory
