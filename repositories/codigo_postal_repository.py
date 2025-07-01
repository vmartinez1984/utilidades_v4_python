from pymongo import MongoClient
from repositories.config import uri

client = MongoClient(uri)
db = client.Utilidades
collection = db["CodigosPostales"]


def get_random_codigo_postal():
    codigo_postal = collection.aggregate([{"$sample": {"size": 1}}]).next()

    return codigo_postal


def get_codigo_postal(codigo_postal):
    codigosPostales = collection.find({"CodigoPostal": codigo_postal})

    return codigosPostales


def get_estados():
    lista = collection.aggregate(
        [
            {"$group": {"_id": {"Estado": "$Estado", "EstadoId": "$EstadoId"}}},
            {"$sort": {"_id.EstadoId": 1}},
        ]
    )
    estados = []
    for item in lista:
        print(item)
        estados.append({"id": item["_id"]["EstadoId"], "nombre": item["_id"]["Estado"]})
    return estados


def get_alcaldias_by_estado(estado: str):
    lista = []
    if estado.isdigit():
        lista = collection.aggregate(
            [
                {"$match": {"EstadoId": int(estado)}},
                {
                    "$group": {
                        "_id": {"Alcaldia": "$Alcaldia", "AlcaldiaId": "$AlcaldiaId"}
                    }
                },
                {"$sort": {"_id.Alcaldia": 1}},
            ]
        )
    else:
        lista = collection.aggregate(
            [
                {"$match": {"Estado": estado}},
                {
                    "$group": {
                        "_id": {"Alcaldia": "$Alcaldia", "AlcaldiaId": "$AlcaldiaId"}
                    }
                },
                {"$sort": {"_id.Alcaldia": 1}},
            ]
        )

    alcaldias = []
    for cp in lista:
        # print(cp)
        alcaldias.append(
            {"id": cp["_id"]["AlcaldiaId"], "nombre": cp["_id"]["Alcaldia"]}
        )

    return alcaldias


def get_estado(estado):
    if estado.isdigit():
        item = collection.find_one({"EstadoId": int(estado)})
    else:
        item = collection.find_one({"Estado": estado})
    # print(item)
    return {"id": item["EstadoId"], "nombre": item["Estado"]}


def get_alcaldia(alcaldia):
    if alcaldia.isdigit():
        item = collection.find_one({"AlcaldiaId": int(alcaldia)})
    else:
        item = collection.find_one({"Alcaldia": alcaldia})
    return {"id": item["AlcaldiaId"], "nombre": item["Alcaldia"]}


def get_codigos_postales_by_alcaldia(estado, alcaldia):
    estado = get_estado(estado)
    alcaldia = get_alcaldia(alcaldia)
    inventory = collection.find(
        {"Estado": estado["nombre"], "Alcaldia": alcaldia["nombre"]}
    )

    return inventory


def search_by_asentamiento(asentamiento: str):
    inventory = collection.find(
        {
            "Asentamiento": {
                "$regex": asentamiento,
                "$options": "i",  # Ignora mayúsculas/minúsculas (opcional)
            }
        }
    )

    return inventory


def search_by_asentamiento_in_estado(estado: str, asentamiento: str):
    estado = get_estado(estado)
    inventory = collection.find(
        {
            "Estado": estado["nombre"],
            "Asentamiento": {
                "$regex": asentamiento,
                "$options": "i",  # Ignora mayúsculas/minúsculas (opcional)
            },
        }
    )
    # print(inventory)
    return inventory


def search_by_asentamiento_in_alcaldia(estado: str, alcaldia: str, asentamiento: str):
    estado = get_estado(estado)
    alcaldia = get_alcaldia(alcaldia)
    inventory = collection.find(
        {
            "Estado": estado["nombre"],
            "Alcaldia": alcaldia["nombre"],
            "Asentamiento": {
                "$regex": asentamiento,
                "$options": "i",  # Ignora mayúsculas/minúsculas (opcional)
            },
        }
    )
    # for item in inventory:
    #     print(item)
    return inventory
