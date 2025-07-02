from typing import Optional
from pydantic import BaseModel
from fastapi import UploadFile, File, Form


class PeliculaDtoIn(BaseModel):
    # titulo:str = Form(...)
    # resumen: str = Form(...)
    # poster: UploadFile = File(...)
    encodedkey: Optional[str] = None
    titulo: str
    resumen: str


class PeliculaDto(BaseModel):
    encodedkey: str
    titulo: str
    resumen: str
    fecha: str
    vista: bool
