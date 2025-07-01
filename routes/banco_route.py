from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from business_layer.banco_bl import (
    create_clabe,
    create_number_card,
    get_plazas,
    get_numeros_de_bancos,
)
from dtos.Banco import (
    ClabeDto,
    NumeroDeBancoDto,
    PlazaDto,
    SolicitudDeClabeDto,
    SolicitudNumeroDeTarjetaDto,
)
from helpers.my_headers import get_headers

banco_router = APIRouter()


@banco_router.post(
    "/clabes",
    summary="Genera clabe",
    response_model=ClabeDto,
    description="La plaza 180 es CDMX y numero de banco 999 es un generico",
)
async def post_clabe(solicitud: SolicitudDeClabeDto):
    clabe = create_clabe(solicitud)

    return {"clabe": clabe, "fecha": str(datetime.now())}


@banco_router.get("/plazas", summary="Lista de plazas", response_model=List[PlazaDto])
async def get_all():
    inventory = get_plazas()
    return JSONResponse(
        headers=get_headers(inventory), status_code=200, content=inventory
    )


@banco_router.post(
    "/NumerosDeTarjetas",
    summary="Obtener numero de tarjeta",
    description="Genera la tarjeta con el BIN 400000",
)
async def router_get_numero_de_tarjeta(solicitud: SolicitudNumeroDeTarjetaDto):
    numero_de_tarjeta = create_number_card(solicitud.numeroDeCuenta)

    return {"numeroDeTarjeta": numero_de_tarjeta, "fecha": str(datetime.now())}


@banco_router.get(
    "/Numeros",
    summary="Lista los numeros de banco y su nombre",
    response_model=List[NumeroDeBancoDto],
)
async def get_all_numeros_de_banco():
    lista = get_numeros_de_bancos()
    return JSONResponse(headers=get_headers(lista), status_code=200, content=lista)
