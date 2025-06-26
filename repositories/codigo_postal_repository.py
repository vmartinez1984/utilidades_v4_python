from pymongo import MongoClient
from repositories.config import uri

client = MongoClient(uri)
db = client.CodigosPostales
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
        estados.append({"id": item["_id"]["EstadoId"], "nombre": item["_id"]["Estado"]})
    return estados


def get_alcaldias_by_estado(estado: str):
    codigos_postales = collection.aggregate(
        [
            {"$match": {"Estado": estado}},
            {"$group": {"_id": {"Alcaldia": "$Alcaldia", "AlcaldiaId": "$AlcaldiaId"}}},
            {"$sort": {"_id.Alcaldia": 1}},
        ]
    )
    alcaldias = []
    for cp in codigos_postales:
        print(cp)
        alcaldias.append(
            {"id": cp["_id"]["AlcaldiaId"], "nombre": cp["_id"]["Alcaldia"]}
        )

    return alcaldias
