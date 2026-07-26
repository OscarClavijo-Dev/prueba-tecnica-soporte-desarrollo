# Nivel 3 — Consumo de API externa

## Objetivo

Integrar una API externa que requiera autenticación y demostrar el consumo,
validación y manejo de errores de la información obtenida.

La API seleccionada fue GitHub API.

## API seleccionada

GitHub API.

Endpoint utilizado:

`GET /user`

Este endpoint permite obtener información del usuario autenticado.

## Mecanismo de autenticación

Se utilizó autenticación mediante Bearer Token.

El token no se encuentra escrito directamente en el código fuente.

La credencial se almacena mediante la variable de entorno:

`GITHUB_TOKEN`

El archivo `.env` está excluido mediante `.gitignore`.

El repositorio únicamente contiene `.env.example`.

## Configuración de credenciales

La credencial utilizada para acceder a GitHub no se almacena directamente
en el código fuente.

El token se configura mediante una variable de entorno:

GITHUB_TOKEN

El archivo `.env` se encuentra excluido del control de versiones mediante
`.gitignore`.

Para facilitar la configuración de nuevos entornos se proporciona un
archivo `.env.example`, sin credenciales reales.

## Implementación

La integración se implementó mediante Python y HTTPX.

Se creó un servicio independiente encargado de realizar las solicitudes
a GitHub:

`app/services/github_service.py`

El servicio obtiene el token desde la configuración de la aplicación y
lo incorpora en el encabezado HTTP Authorization utilizando el esquema
Bearer.

El servicio utiliza un cliente HTTP asíncrono y establece un tiempo máximo
de espera de 10 segundos para evitar solicitudes indefinidamente bloqueadas.

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {settings.github_token}",
    "X-GitHub-Api-Version": "2022-11-28",
}

### Encabezados utilizados

- `Accept`: indica el formato esperado de la respuesta.
- `Authorization`: contiene el Bearer Token utilizado para autenticación.
- `X-GitHub-Api-Version`: establece explícitamente la versión de la API.


## Prueba de integración

La prueba se ejecutó desde la terminal de Fedora utilizando el entorno
virtual de Python.

Comando:

```bash
python -m scripts.test_github
```
Usuario autenticado:
{
    'login': 'OscarClavijo-Dev',
    ...
}

```text
docs/
└── evidencias/
``` 

## Manejo de errores

La implementación utiliza `response.raise_for_status()` para detectar
respuestas HTTP que representan errores.

Por ejemplo:

- `401`: credenciales inválidas o ausentes.
- `403`: solicitud no autorizada o restricciones de acceso.
- `404`: recurso no encontrado.
- `429`: límite de solicitudes alcanzado.
- `5xx`: error del servidor remoto.

También se estableció un timeout de 10 segundos para evitar que una
solicitud quede esperando indefinidamente.

## Flujo de autenticación

```text
Aplicación
    |
    | obtiene GITHUB_TOKEN
    ↓
Variables de entorno
    |
    ↓
HTTPX
    |
    | Authorization: Bearer TOKEN
    ↓
GitHub API
    |
    ↓
Respuesta JSON