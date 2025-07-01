from typing import Optional
from pydantic import BaseModel


class PlazaDto(BaseModel):
    id: int
    nombre: str


class SolicitudDeClabeDto(BaseModel):
    depositoId: str
    plaza: int = 180
    numeroDeBanco: int = 999


class NumeroDeBancoDto(BaseModel):
    numero: int
    nombreAbreviado: str
    nombreDeInstitucion: str


class ClabeDto(BaseModel):
    clabe: str
    fecha: str


class SolicitudNumeroDeTarjetaDto(BaseModel):
    numeroDeCuenta: Optional[str] = None
