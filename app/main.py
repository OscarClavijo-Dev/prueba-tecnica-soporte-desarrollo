from fastapi import FastAPI

app = FastAPI(
    title="Prueba Tecnica - API",
    description="API desarrollada como parte de la prueba tecnica.",
    version="1.0.0"
)

@app.get("/")
def root():
    return{
        "message": "Bienvenido a la API de la prueba Tecnica"
    }

@app.get("/health")
def health():
    return{
        "status": "ok"
    }