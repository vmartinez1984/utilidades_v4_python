from datetime import datetime
from typing import List
import uuid
from dtos.PeliculaDto import PeliculaDto
from repositories.pelicula_repository import add, get_all, get_by_encodedkey_repo


def add_pelicula(pelicula: PeliculaDto) -> str:
    pelicula = dict(pelicula)
    if pelicula["encodedkey"] == None:
        pelicula["encodedkey"] = str(uuid.uuid4())
    pelicula["fecha"] = datetime.now()
    pelicula["vista"] = False
    add(pelicula)

    return pelicula["encodedkey"]


def get_peliculas_bl(vista: bool = False) -> List[PeliculaDto]:
    inventory = get_all(vista)
    peliculas = []
    for item in inventory:
        peliculas.append(
            {
                "encodekey": item["encodedkey"],
                "titulo": item["titulo"],
                "resumen": item["resumen"],
                "fecha": str(item["fecha"]),
                "vista": item["vista"],
            }
        )

    return peliculas


def get_pelicula_by_encodedkey_bl(encodedkey: str) -> PeliculaDto:
    item = get_by_encodedkey_repo(encodedkey)
    pelicula = None
    if item != None:    
        pelicula = {
            "encodekey": item["encodedkey"],
            "titulo": item["titulo"],
            "resumen": item["resumen"],
            "fecha": str(item["fecha"]),
            "vista": item["vista"],
        }

    return pelicula