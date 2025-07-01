from fastapi import FastAPI

from routes.codigo_postal_route import codigo_postal_router
from routes.pelicula_route import pelicula_router
from routes.banco_route import banco_router

app = FastAPI(title="Utilerias v4", description="Conjunto de herramientas para pruebas")

app.include_router(
    codigo_postal_router, prefix="/api/CodigosPostales", tags=["Códigos postales"]
)

app.include_router(pelicula_router, prefix="/api/Peliculas", tags=["Peliculas"])

app.include_router(banco_router, prefix="/api/Bancos", tags=["Banco"])
