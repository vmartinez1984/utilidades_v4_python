
from pydantic import BaseModel

class IdDto(BaseModel):
    mensaje:str
    encodekey: str
    fecha: str