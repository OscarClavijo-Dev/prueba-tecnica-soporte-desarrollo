# Pruebas de la API REST propia — Nivel 5

## 1. Objetivo

Este documento registra las pruebas funcionales realizadas sobre la API REST propia desarrollada para el Nivel 5 de la prueba técnica.

La API permite consultar y gestionar los usuarios almacenados en PostgreSQL mediante operaciones HTTP.

La implementación utiliza:

* FastAPI
* SQLAlchemy 2.0
* PostgreSQL 17
* Pydantic
* Uvicorn
* Insomnia
* cURL
* Swagger / OpenAPI

La API implementa operaciones CRUD, filtros, paginación, validación de datos y manejo de errores HTTP.

---

# 2. Resumen de pruebas

| #  | Método | Endpoint          | Prueba                         | Resultado |
| -- | ------ | ----------------- | ------------------------------ | --------- |
| 1  | GET    | `/`               | Estado básico de la aplicación | ✅ 200     |
| 2  | GET    | `/api/users`      | Consultar usuarios             | ✅ 200     |
| 3  | GET    | `/api/users/{id}` | Consultar usuario por ID       | ✅ 200     |
| 4  | GET    | `/api/users/{id}` | ID inexistente                 | ✅ 404     |
| 5  | GET    | `/api/users`      | Filtrar por login/nombre/email | ✅ 200     |
| 6  | GET    | `/api/users`      | Paginación                     | ✅ 200     |
| 7  | POST   | `/api/users`      | Crear usuario                  | ✅ 201     |
| 8  | POST   | `/api/users`      | Usuario duplicado              | ✅ 409     |
| 9  | POST   | `/api/users`      | Datos inválidos                | ✅ 422     |
| 10 | PUT    | `/api/users/{id}` | Actualizar usuario             | ✅ 200     |
| 11 | GET    | `/api/users/{id}` | Verificar persistencia del PUT | ✅ 200     |
| 12 | DELETE | `/api/users/{id}` | Eliminar usuario               | ✅ 204     |
| 13 | GET    | `/api/users/{id}` | Verificar eliminación          | ✅ 404     |

---

# 3. Prueba GET `/`

## Objetivo

Verificar que la aplicación FastAPI se encuentre disponible.

## Solicitud

```bash
curl http://127.0.0.1:8000/
```

## Respuesta

```json
{
  "message": "Bienvenido a la API de la prueba Tecnica"
}
```

## Resultado

```text
HTTP 200 OK
```

La respuesta confirma que la aplicación se encuentra levantada y atendiendo solicitudes HTTP.

---

# 4. Prueba GET `/api/users`

## Objetivo

Consultar todos los usuarios almacenados en PostgreSQL.

## Solicitud

```bash
curl http://127.0.0.1:8000/api/users
```

## Resultado esperado

```text
HTTP 200 OK
```

La API devuelve una colección JSON con los usuarios persistidos.

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-01-get-users.png
```

---

# 5. Prueba GET `/api/users/{id}`

## Objetivo

Consultar un usuario específico mediante su identificador interno.

## Solicitud

```bash
curl http://127.0.0.1:8000/api/users/19
```

## Resultado esperado

```text
HTTP 200 OK
```

La respuesta contiene información del usuario y sus campos de auditoría:

* `id`
* `github_id`
* `login`
* `name`
* `email`
* `avatar_url`
* `html_url`
* `created_at`
* `updated_at`

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-02-get-by-id.png
```

---

# 6. Prueba de usuario inexistente

## Objetivo

Comprobar que la API maneja correctamente la consulta de un identificador inexistente.

## Solicitud

```bash
curl http://127.0.0.1:8000/api/users/999999
```

## Resultado esperado

```json
{
  "detail": "Usuario no encontrado"
}
```

## Código HTTP

```text
404 Not Found
```

Este comportamiento evita devolver un `500 Internal Server Error` cuando el recurso simplemente no existe.

### Evidencia

```text
docs/evidencias/nivel-5/Prueba-API-GEt_user_id_id_noexiste.png
```

---

# 7. Prueba de filtros

El endpoint `GET /api/users` permite aplicar filtros opcionales.

Parámetros disponibles:

```text
login
name
email
```

Ejemplo:

```bash
curl "http://127.0.0.1:8000/api/users?login=nivel5"
```

También se puede combinar con paginación:

```bash
curl "http://127.0.0.1:8000/api/users?login=nivel5&skip=0&limit=10"
```

## Resultado

```text
HTTP 200 OK
```

Los filtros utilizan búsqueda parcial mediante `ILIKE`, permitiendo localizar registros sin exigir coincidencia exacta.

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-03-filtro.png
```

---

# 8. Prueba de paginación

La API utiliza:

```text
skip
limit
```

Ejemplo:

```bash
curl "http://127.0.0.1:8000/api/users?skip=0&limit=2"
```

La implementación establece:

* `skip >= 0`
* `limit >= 1`
* `limit <= 100`

Esto evita valores negativos y limita la cantidad máxima de registros devueltos en una solicitud.

### Evidencia

```text
docs/evidencias/nivel-5/PruebaAPI-nivel5-paginacion.png
```

---

# 9. Prueba POST `/api/users`

## Objetivo

Crear un nuevo usuario en PostgreSQL.

## Solicitud

```bash
curl -X POST "http://127.0.0.1:8000/api/users" \
  -H "Content-Type: application/json" \
  -d '{
    "github_id": 987654324,
    "login": "nivel5-test-02",
    "name": "Nivel 5 Test 02",
    "email": "nivel5-test-02@example.com",
    "avatar_url": "https://example.com/avatar2.png",
    "html_url": "https://github.com/nivel5-test-02"
  }'
```

## Resultado

```text
HTTP 201 Created
```

La API devuelve el registro creado junto con:

```text
id
created_at
updated_at
```

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-04-post.png
```

---

# 10. Incidencia inicial del POST — HTTP 500

Durante la primera ejecución de `POST /api/users` se produjo un error interno.

El primer problema detectado fue:

```text
UnboundLocalError:
cannot access local variable 'exc'
where it is not associated with a value
```

## Diagnóstico

El router intentaba acceder a una variable de excepción fuera del contexto correcto de manejo de excepciones.

Se corrigió la estructura del bloque:

```python
except IntegrityError as exc:
```

de forma que `exc` solamente se utilice dentro del bloque donde está definida.

---

# 11. Incidencia PostgreSQL — NOT NULL

Después de solucionar el primer error apareció:

```text
psycopg2.errors.NotNullViolation:
null value in column "created_at"
of relation "github_users"
violates not-null constraint
```

PostgreSQL mostró:

```text
created_at = null
updated_at = null
```

## Causa

Las columnas estaban definidas como obligatorias en PostgreSQL, pero la aplicación estaba intentando insertar `NULL`.

## Solución

Se modificó el modelo y la capa de servicio para garantizar la creación de timestamps UTC.

La creación del registro pasó a generar:

```python
now = datetime.now(timezone.utc)
```

y utilizar el valor para:

```text
created_at
updated_at
```

Esto garantiza que un registro nuevo posea fechas de auditoría válidas.

---

# 12. Incidencia HTTP 409 — registro duplicado

Durante las pruebas posteriores apareció:

```text
409 Conflict
```

La API respondió indicando que ya existía un usuario con el mismo `github_id`.

## Diagnóstico

La restricción de unicidad de PostgreSQL sobre:

```text
github_id
```

impide registrar dos usuarios con el mismo identificador externo.

La consulta previa implementada en el router:

```python
existing_user = user_service.get_user_by_github_id(
    db,
    user_data.github_id,
)
```

permite detectar el conflicto antes de intentar insertar.

## Comportamiento esperado

```json
{
  "detail": "Ya existe un usuario con ese github_id"
}
```

## Código HTTP

```text
409 Conflict
```

## Solución durante la prueba

Se utilizó un `github_id` diferente:

```text
987654324
```

Con el nuevo identificador la operación fue procesada correctamente.

Esta prueba confirmó que el `409` no representaba un fallo de FastAPI, sino un conflicto real de datos provocado por la unicidad del identificador externo.

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-08-duplicado-409.png
```

---

# 13. Prueba de validación — HTTP 422

Se realizó una prueba enviando información que no cumplía las restricciones del esquema Pydantic.

La API respondió:

```text
422 Unprocessable Entity
```

Este comportamiento es generado por FastAPI/Pydantic antes de ejecutar la lógica de persistencia cuando los datos no cumplen el contrato definido.

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-09-validacion-422.png
```

---

# 14. Prueba PUT `/api/users/{id}`

## Objetivo

Actualizar información de un usuario existente.

Ejemplo:

```http
PUT /api/users/19
```

Payload:

```json
{
  "name": "Nivel 5 Test 02 Actualizado",
  "email": "nivel5-updated@example.com"
}
```

## Resultado

```text
HTTP 200 OK
```

El campo:

```text
updated_at
```

se actualiza para registrar el momento de modificación.

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-05-put.png
```

---

# 15. Verificación de persistencia del PUT

Posteriormente se realizó:

```http
GET /api/users/19
```

La API devolvió los valores modificados.

Esto permitió comprobar que el cambio no solamente estaba presente en la respuesta inmediata del PUT, sino que quedó persistido en PostgreSQL.

### Evidencia

```text
docs/evidencias/nivel-5/PruebaAPI_persistencia_PUT_GET.png
```

---

# 16. Verificación directa en PostgreSQL

Se ejecutó:

```sql
SELECT
    id,
    github_id,
    login,
    name,
    email,
    created_at,
    updated_at
FROM github_users
ORDER BY id DESC
LIMIT 10;
```

Se verificó que el registro actualizado contiene:

```text
19 | 987654324 | nivel5-test-02 |
Nivel 5 Test 02 Actualizado |
nivel5-updated@example.com
```

Además:

```text
updated_at > created_at
```

confirmando que la actualización fue persistida correctamente.

---

# 17. Prueba DELETE `/api/users/{id}`

## Objetivo

Eliminar un usuario existente.

## Resultado esperado

```text
HTTP 204 No Content
```

El código `204` indica que la operación fue realizada correctamente y no requiere contenido en el cuerpo de la respuesta.

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-06-delete.png
```

---

# 18. Verificación posterior al DELETE

Después de eliminar el registro se realizó nuevamente:

```http
GET /api/users/{id}
```

El resultado esperado fue:

```text
404 Not Found
```

Esto demuestra que el registro realmente dejó de estar disponible mediante la API.

### Evidencia

```text
docs/evidencias/nivel-5/nivel-5-insomnia-07-delete-verificacion.png
```

---

# 19. Validación mediante Insomnia

Las pruebas funcionales fueron repetidas utilizando Insomnia como cliente HTTP.

Se validaron:

* GET de colección.
* GET por identificador.
* Filtros.
* POST.
* PUT.
* DELETE.
* Respuesta 404.
* Respuesta 409.
* Respuesta 422.

Las evidencias visuales se encuentran en:

```text
docs/evidencias/nivel-5/
```

---

# 20. Validación mediante cURL

También se realizaron pruebas mediante cURL desde Fedora.

Ejemplo:

```bash
curl http://127.0.0.1:8000/
```

Resultado:

```json
{
  "message": "Bienvenido a la API de la prueba Tecnica"
}
```

También se validó la documentación:

```bash
curl http://127.0.0.1:8000/docs
```

La respuesta corresponde al documento HTML generado por Swagger UI.

---

# 21. Validación de compilación

Se ejecutó:

```bash
python -m compileall app
```

Resultado:

```text
Listing 'app'...
Listing 'app/api'...
Listing 'app/core'...
Listing 'app/database'...
Listing 'app/models'...
Listing 'app/routers'...
Listing 'app/schemas'...
Listing 'app/services'...
Listing 'app/utils'...
```

No se presentaron errores de compilación.

---

# 22. Validación de calidad del diff

Se ejecutó:

```bash
git diff --check
```

El comando no produjo salida, indicando que no se detectaron problemas de whitespace en los cambios revisados.

---

# 23. Conclusión

El Nivel 5 fue validado mediante pruebas funcionales utilizando Swagger/OpenAPI, Insomnia, cURL y consultas directas a PostgreSQL.

La API permite:

* Consultar registros.
* Consultar un registro por identificador.
* Crear registros.
* Actualizar registros.
* Eliminar registros.
* Filtrar información.
* Paginar resultados.
* Validar datos de entrada.
* Gestionar recursos inexistentes.
* Gestionar conflictos de unicidad.
* Persistir información en PostgreSQL.
* Documentar automáticamente sus operaciones mediante OpenAPI.

Los errores encontrados durante la implementación fueron registrados y corregidos, incluyendo:

* `UnboundLocalError`
* `HTTP 500`
* `NOT NULL violation`
* `HTTP 409 Conflict`
* `HTTP 422 Unprocessable Entity`
* Errores de mapeo ORM de SQLAlchemy

Con las pruebas realizadas, el Nivel 5 se considera funcionalmente completado.
