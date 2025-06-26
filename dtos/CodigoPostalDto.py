from pydantic import BaseModel

class CodigoPostalDto(BaseModel):
    codigoPostal: str
    alcaldiaId: int
    estado: str
    estadoId: int
    alcaldia: str
    tipoDeAsentamiento: str
    asentamiento: str

class AlcaldiaDto(BaseModel):
    id: int
    nombre: str

class EstadoDto(BaseModel):
    id: int
    nombre: str