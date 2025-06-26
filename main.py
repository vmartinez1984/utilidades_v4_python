from fastapi import FastAPI

from routes.codigo_postal_route import codigo_postal_router

app= FastAPI()

app.include_router(codigo_postal_router, prefix="/api/CodigosPostales")
