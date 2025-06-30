from fastapi import APIRouter

pelicula_router = APIRouter()

@pelicula_router.get("/movies")
async def get():

    return ""

@pelicula_router.post("/movies")
async def post():
    
    return ""