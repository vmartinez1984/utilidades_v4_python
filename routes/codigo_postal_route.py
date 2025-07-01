from typing import List
from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from helpers import my_headers
from repositories.codigo_postal_repository import (
    get_random_codigo_postal,
    get_codigo_postal,
    get_alcaldias_by_estado,
    get_estados,
    get_codigos_postales_by_alcaldia,
    search_by_asentamiento,
    search_by_asentamiento_in_estado,
    search_by_asentamiento_in_alcaldia,
)

# from repositories.estado_repository import get_estados
from dtos.CodigoPostalDto import AlcaldiaDto, CodigoPostalDto, EstadoDto
from helpers.mapper import serial_codigo_postal, serial_codigos_postales

codigo_postal_router = APIRouter()


@codigo_postal_router.get(
    "/Estados",
    response_model=List[EstadoDto],
    description="Devuelve una lista de los estados de la republica mexicana",
    summary="Lista de estados",
)
async def get_list_estados():
    estados = get_estados()

    return estados


@codigo_postal_router.get(
    "/Estados/{estado}/Alcaldias",
    response_model=List[AlcaldiaDto],
    summary="Lista de alcaldias por estado o estadoId",
)
async def get_list_alcaldias(estado: str = Path(..., min_length=1)):
    print(estado)
    lista = get_alcaldias_by_estado(estado)
    if len(lista) == 0:
        return JSONResponse(
            content={"message": "No se encontro el estado: " + estado}, status_code=404
        )

    return JSONResponse(
        content=lista, status_code=200, headers={"total": str(len(lista))}
    )


@codigo_postal_router.get(
    "/Estados/{estado}/Asentamientos/{asentamiento}",
    response_model=List[CodigoPostalDto],
    summary="Buscar la colonia/asentamiento en un estado o estadoId",
)
async def get_by_asentamiento_in_estado(estado: str, asentamiento: str):
    inventory = search_by_asentamiento_in_estado(estado, asentamiento)
    # print(inventory)
    inventory = serial_codigos_postales(inventory)
    # print(inventory)
    return JSONResponse(
        status_code=200, content=inventory, headers=my_headers(inventory)
    )


@codigo_postal_router.get(
    "/Estados/{estado}/Alcaldias/{alcaldia}",
    summary="Lista de codigos postales de una alcaldia",
    response_model=List[CodigoPostalDto],
)
async def get_codigos_by_estado_and_alcaldia(estado, alcaldia):
    codigos = get_codigos_postales_by_alcaldia(estado, alcaldia)
    # for item in codigos:
    #     print(item)
    codigos = serial_codigos_postales(codigos)
    return JSONResponse(content=codigos, status_code=200)


@codigo_postal_router.get(
    "/Estados/{estado}/Alcaldias/{alcaldia}/Asentamientos/{asentamiento}",
    summary="Busqueda de colonia/asentamiento en una alcaldia",
    response_model=List[CodigoPostalDto],
)
async def get_codigos_postales_by_asentamiento_in_alcaldia(
    estado: str, alcaldia: str, asentamiento: str
):
    inventory = search_by_asentamiento_in_alcaldia(estado, alcaldia, asentamiento)
    inventory = serial_codigos_postales(inventory)

    return JSONResponse(
        content=inventory, status_code=200, headers=my_headers(inventory)
    )


@codigo_postal_router.get(
    "/Aleatorio", response_model=CodigoPostalDto, summary="Codigo postal aleatorio"
)
async def get_ramdom():
    print("Aleatorio")
    codigo_postal = get_random_codigo_postal()
    codigo_postal = serial_codigo_postal(codigo_postal)

    return codigo_postal


@codigo_postal_router.get(
    "/Asentamientos/{asentamiento}",
    summary="Busqueda por colonia/asentamiento",
    response_model=List[CodigoPostalDto],
)
async def search_asentamiento(asentamiento: str):
    inventory = search_by_asentamiento(asentamiento)
    # for item in inventory:
    #     print(item)
    inventory = serial_codigos_postales(inventory)

    return JSONResponse(content=inventory, headers={"total": str(len(inventory))})


@codigo_postal_router.get(
    "/{codigoPostal}",
    response_model=List[CodigoPostalDto],
    summary="Lista de codigos postales",
)
async def get_by_codigo_postal(codigoPostal: str):
    lista = get_codigo_postal(codigoPostal)
    lista = serial_codigos_postales(lista)

    return lista
