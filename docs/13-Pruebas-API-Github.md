# 13 - Pruebas de integración con GitHub API

## 1. Objetivo

Validar la integración entre la API desarrollada con FastAPI y la API REST de GitHub mediante autenticación con Bearer Token.

La prueba busca comprobar que:

- FastAPI se encuentra disponible.
- El endpoint interno responde correctamente.
- FastAPI puede comunicarse con GitHub.
- La credencial configurada permite realizar una solicitud autenticada.
- La información recibida puede ser devuelta al cliente.

---

## 2. Arquitectura de la prueba

```text
Cliente / curl
      |
      v
FastAPI
      |
      v
GET /api/github/me
      |
      v
github_service.py
      |
      | Authorization: Bearer <token>
      v
GitHub REST API
      |
      v
Información del usuario autenticado

```