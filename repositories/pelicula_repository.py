from bson import ObjectId
from pymongo import MongoClient
from repositories.config import uri

client = MongoClient(uri)
db = client.Utilidades
collection = db["Peliculas"]


def add(pelicula):
    pelicula = dict(pelicula)
    pelicula["id"] = get_id()
    data = collection.insert_one(pelicula)

    return str(data.inserted_id)


def get_id():
    ultimo = collection.find().sort("_id", -1).limit(1)
    if ultimo == None:
        return 1
    else:
        return ultimo["id"] + 1


def get_all(isViewed: bool = True):
    inventory = collection.find({"isViewed": isViewed})

    return inventory


def update(pelicula):
    collection.find_one_and_update(
        {"_id": ObjectId(pelicula["_id"])}, {"$set": dict(pelicula)}
    )
