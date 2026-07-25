## Preparación del entorno

Se creó un entorno virtual de Python para aislar las dependencias del proyecto del sistema operativo.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Posteriormente se instalaron las dependencias iniciales necesarias para el desarrollo de la API:

- FastAPI
- Uvicorn
- SQLAlchemy
- psycopg2-binary
- python-dotenv
- Pydantic

Finalmente se generó el archivo `requirements.txt` utilizando:

```bash
pip freeze > requirements.txt
```

Esto garantiza que cualquier desarrollador pueda reconstruir el mismo entorno ejecutando:

```bash
pip install -r requirements.txt
```

## Primer endpoint

Se implementaron dos endpoints iniciales:

| Método | Ruta | Descripción |
|---------|------|-------------|
| GET | / | Mensaje de bienvenida |
| GET | /health | Verificación del estado de la API |

FastAPI genera automáticamente la documentación interactiva en:

- /docs (Swagger UI)
- /redoc (ReDoc)

Estas herramientas permiten probar los endpoints sin necesidad de desarrollar un cliente adicional.