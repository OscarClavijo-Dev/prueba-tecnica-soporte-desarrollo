# API REST propia — Nivel 5

## 1. Objetivo

El Nivel 5 consiste en desarrollar una API propia que permita consultar y
gestionar la información almacenada previamente en PostgreSQL.

La implementación se realizó utilizando FastAPI, SQLAlchemy 2.0, Pydantic y
PostgreSQL 17.

La API permite consultar, crear, actualizar, eliminar y filtrar usuarios
almacenados en la tabla `github_users`.

---

## 2. Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- SQLAlchemy 2.0
- Pydantic
- PostgreSQL 17
- Docker
- Swagger UI / OpenAPI
- Insomnia
- cURL

---

## 3. Arquitectura

La API mantiene separación de responsabilidades entre:

```text
HTTP Request
     │
     ▼
Router
     │
     ▼
Schema / Pydantic
     │
     ▼
Service
     │
     ▼
SQLAlchemy ORM
     │
     ▼
PostgreSQL

```

## Responsabilidades
# Router

- Los routers reciben las solicitudes HTTP, validan parámetros de entrada,
determinan el código HTTP correspondiente y delegan la operación al servicio.

# Archivo principal:
```text
app/routers/users.py
Schemas
```

- Los schemas Pydantic definen la estructura y validaciones de los datos
recibidos y enviados por la API.

Archivo:

```text
app/schemas/user.py
Service
```

La capa de servicios concentra las operaciones de acceso y modificación de
datos.

Archivo:
```text

app/services/user_service.py
Model

```

- SQLAlchemy representa la tabla github_users como un modelo ORM.

Archivo:

```text
app/models/github_user.py
```
# 4. Endpoints implementados

## GET /api/users

### Consulta todos los usuarios almacenados.

Permite filtros opcionales mediante:

login
name
email

También soporta paginación mediante:

skip
limit

Ejemplo:

 ```text
curl "http://127.0.0.1:8000/api/users"
```

Ejemplo con filtro:

```text
curl "http://127.0.0.1:8000/api/users?login=nivel5"
```

Ejemplo con paginación:

```text
curl "http://127.0.0.1:8000/api/users?skip=0&limit=10"
```

Respuesta esperada:

```text
200 OK
GET /api/users/{user_id}
```

Consulta un usuario mediante su identificador interno.

Ejemplo:

```text
curl http://127.0.0.1:8000/api/users/19
```

Respuesta esperada:

```text
200 OK
```
Si el identificador no existe:

```text
404 Not Found
POST /api/users
```

# Crea un nuevo usuario.

Ejemplo:

```text
{
  "github_id": 987654324,
  "login": "nivel5-test-02",
  "name": "Nivel 5 Test 02",
  "email": "nivel5-test-02@example.com",
  "avatar_url": "https://example.com/avatar2.png",
  "html_url": "https://github.com/nivel5-test-02"
}
```

Respuesta esperada:

```text
201 Created
```

- La respuesta incluye:

id
github_id
login
name
email
avatar_url
html_url
created_at
updated_at
PUT /api/users/{user_id}

Actualiza los datos de un usuario existente.

Ejemplo:

```text
curl -X PUT \
  http://127.0.0.1:8000/api/users/19 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Nivel 5 Test 02 Actualizado",
    "email": "nivel5-updated@example.com"
  }'
```
Respuesta esperada:

```text
200 OK
```

- La persistencia del cambio fue comprobada posteriormente directamente en
PostgreSQL.

```text
DELETE /api/users/{user_id}
```

Elimina un usuario existente.

Ejemplo:

```text
curl -X DELETE \
  http://127.0.0.1:8000/api/users/20
```

Respuesta esperada:

```text
204 No Content
```

Posteriormente se puede consultar nuevamente el recurso para verificar que ya
no existe.

## 5. Validaciones

- La API utiliza Pydantic para validar los datos recibidos.

Por ejemplo:

```text
github_id: int = Field(..., gt=0)
```

Esto impide recibir valores de github_id menores o iguales a cero.

También se validan:

* longitud mínima de login
* longitud máxima de login
* longitud máxima de name
* longitud máxima de email
* tipos de datos
* campos obligatorios

Cuando los datos enviados no cumplen las reglas definidas, FastAPI responde:
```text
422 Unprocessable Entity
```

## 6. Manejo de duplicados

- El campo github_id posee una restricción UNIQUE en PostgreSQL.

La API realiza una consulta previa antes de insertar:

```text
existing_user = user_service.get_user_by_github_id(
    db,
    user_data.github_id,
)
```

- Si el usuario ya existe, se responde:

```text
409 Conflict
```

-Esto evita crear registros duplicados.

-También se mantiene el manejo de IntegrityError como protección adicional
ante una posible condición de carrera entre solicitudes concurrentes.

## 7. Manejo de transacciones

- Cuando ocurre un error durante una operación de base de datos, se realiza:

```text
db.rollback()
```

Esto permite revertir la transacción fallida y evitar que la sesión SQLAlchemy
permanezca en un estado inválido.

Durante las pruebas del Nivel 5 se identificó específicamente una incidencia
relacionada con los campos temporales created_at y updated_at.

La incidencia fue investigada mediante los logs de Uvicorn y PostgreSQL y
posteriormente corregida.

## 8. Documentación interactiva

FastAPI genera automáticamente documentación OpenAPI.

Swagger UI está disponible en:
```text
http://127.0.0.1:8000/docs
```
También se dispone del esquema OpenAPI:
```text
http://127.0.0.1:8000/openapi.json
```
## 9. Estado de la API

- La API implementada cubre las operaciones principales solicitadas para el
Nivel 5:

| Funcionalidad | Estado |
| :--- | :--- |
| Consultar todos los registros | Implementado |
| Consultar por identificador | Implementado |
| Crear registros | Implementado |
| Actualizar registros | Implementado |
| Eliminar registros | Implementado |
| Buscar / filtrar | Implementado |
| Paginación | Implementado |
| Validación de datos | Implementado |
| Manejo de duplicados | Implementado |
| Swagger / OpenAPI | Implementado |
| Pruebas con curl | Realizadas |
| Pruebas con Insomnia | Realizadas |

## 10. Evidencias

-Las capturas de las pruebas se encuentran en:

```text
docs/evidencias/nivel-5/
```

- Se incluyen evidencias de:

* GET de usuarios
* GET por identificador
* filtros
* paginación
* POST
* PUT
* DELETE
* validaciones
* usuario duplicado
* persistencia de cambios*

## 11. Resultado

El Nivel 5 se considera funcionalmente completado.

La API permite gestionar la información almacenada en PostgreSQL mediante
endpoints REST documentados y probados.

Las pruebas fueron realizadas mediante Swagger UI, Insomnia, cURL y consultas
directas a PostgreSQL.