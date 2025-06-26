from typing import List
from fastapi import APIRouter
from repositories.codigo_postal_repository import (
    get_random_codigo_postal,
    get_codigo_postal,
    get_alcaldias_by_estado,
    get_estados,
)

# from repositories.estado_repository import get_estados
from dtos.CodigoPostalDto import AlcaldiaDto, CodigoPostalDto, EstadoDto
from helpers.mapper import serial_codigo_postal, serial_codigos_postales

codigo_postal_router = APIRouter()


@codigo_postal_router.get("/Estados", response_model=EstadoDto)
async def get_list_estados():
    estados = get_estados()
    return estados


@codigo_postal_router.get("/{estado}/Alcaldias", response_model=AlcaldiaDto)
async def get_list_alcaldias(estado):
    lista = get_alcaldias_by_estado(estado)

    return lista


@codigo_postal_router.get("/Aleatorio", response_model=CodigoPostalDto)
async def get_ramdom():
    print("Aleatorio")
    codigo_postal = get_random_codigo_postal()
    codigo_postal = serial_codigo_postal(codigo_postal)

    return codigo_postal


@codigo_postal_router.get("/{codigoPostal}", response_model=List[CodigoPostalDto])
async def get_by_codigo_postal(codigoPostal: str):
    lista = get_codigo_postal(codigoPostal)
    lista = serial_codigos_postales(lista)

    return lista
