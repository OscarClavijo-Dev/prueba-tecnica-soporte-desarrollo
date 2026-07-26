# Flujo de autenticación - GitHub API

## Objetivo

Documentar el mecanismo utilizado para autenticar las solicitudes realizadas
desde la API propia hacia GitHub.

## Mecanismo utilizado

La integración utiliza un Personal Access Token de GitHub enviado mediante
el esquema de autenticación Bearer.

La credencial no se almacena directamente en el código fuente.

Se almacena mediante la variable de entorno:

GITHUB_TOKEN

Esta variable es cargada por la aplicación mediante Pydantic Settings.

## Flujo

El flujo de comunicación es el siguiente:

1. El cliente realiza una solicitud a FastAPI.
2. FastAPI recibe la solicitud en el endpoint `/api/github/me`.
3. El endpoint invoca el servicio de GitHub.
4. El servicio obtiene la credencial desde la configuración de la aplicación.
5. FastAPI construye el encabezado Authorization.
6. Se realiza una solicitud HTTPS a GitHub.
7. GitHub valida el token.
8. GitHub devuelve la información del usuario autenticado.
9. FastAPI devuelve la respuesta al cliente.

## Encabezados utilizados

```http
Accept: application/vnd.github+json
Authorization: Bearer <TOKEN>
X-GitHub-Api-Version: 2022-11-28
```