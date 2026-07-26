from fastapi import FastAPI

from app.routers.github import router as github_router


app = FastAPI(
    title="Prueba Técnica - API",
    description="API desarrollada para la prueba técnica de Soporte y Desarrollo.",
    version="1.0.0",
)


app.include_router(github_router)


@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de la prueba Tecnica"}