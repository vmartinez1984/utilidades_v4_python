from fastapi import FastAPI

from routes.codigo_postal_route import codigo_postal_router

app= FastAPI(
    title="Utilerias v4",
    description="Conjunto de herramientas para pruebas"
)

app.include_router(codigo_postal_router, prefix="/api/CodigosPostales", tags=["Códigos postales"])
