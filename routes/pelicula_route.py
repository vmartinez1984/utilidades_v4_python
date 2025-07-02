from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from business_layer.pelicula_bl import (
    add_pelicula,
    get_pelicula_by_encodedkey_bl,
    get_peliculas_bl,
)
from dtos.IdDto import IdDto
from dtos.PeliculaDto import PeliculaDtoIn, PeliculaDto
from helpers.my_headers import get_headers

pelicula_router = APIRouter()


@pelicula_router.get(
    "/", response_model=List[PeliculaDto], summary="Lista de peliculas"
)
async def get(vista: bool = False):
    lista = get_peliculas_bl(vista)
    return JSONResponse(content=lista, headers=get_headers(lista))


@pelicula_router.post("/", response_model=IdDto, summary="Agregar pelicula")
async def post(pelicula: PeliculaDtoIn):
    if pelicula.encodedkey != None:
        pelicula = get_pelicula_by_encodedkey_bl(pelicula.encodedkey)
        if pelicula != None:
            return JSONResponse(content=pelicula, status_code=200)
        
    encodedkey = add_pelicula(pelicula)
    return JSONResponse(
        content={
            "mensaje": "Pelicula agregada",
            "encodedkey": encodedkey,
            "fecha": str(datetime.now()),
        },
        status_code=201
    )


@pelicula_router.get(
    "/{encodedkey}", summary="Pelicula por encodedkey", response_model=PeliculaDto
)
async def get_by_encodedkey_route(encodedkey: str):
    pelicula = get_pelicula_by_encodedkey_bl(encodedkey)
    if pelicula == None:
        return JSONResponse(
            content={
                "mensaje": "Pelicula no encontrada",
                "encodedkey": encodedkey,
                "fecha": str(datetime.now()),
            },
            status_code=404,
        )

    return JSONResponse(
        content=pelicula,
        status_code=200,
    )
