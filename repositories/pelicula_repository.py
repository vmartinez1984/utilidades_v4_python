from bson import ObjectId
from pymongo import MongoClient
from repositories.config import uri, db_name

client = MongoClient(uri)
db = client[db_name]
collection = db["Peliculas"]


def add(pelicula):
    pelicula = dict(pelicula)
    pelicula["id"] = get_id()
    data = collection.insert_one(pelicula)

    return str(data.inserted_id)


def get_id():
    ultimo = collection.find().sort("_id", -1).limit(1)
    resultado = list(ultimo)

    if not resultado:
        return 1
    else:
        return resultado[0]["id"] + 1


def get_all(vista: bool = False):
    inventory = collection.find({"vista": vista})

    return inventory


def update(pelicula):
    collection.find_one_and_update(
        {"_id": ObjectId(pelicula["_id"])}, {"$set": dict(pelicula)}
    )


def get_by_encodedkey_repo(encodedkey:str):
    item = collection.find_one({"encodedkey":encodedkey})

    return item