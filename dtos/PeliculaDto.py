from pydantic import BaseModel
from fastapi import UploadFile, File, Form

class PeliculaDtoIn(BaseModel):
    titulo:str = Form(...)
    resumen: str = Form(...)
    poster: UploadFile = File(...)