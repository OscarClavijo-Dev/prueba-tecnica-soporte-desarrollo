# Diagrama de integración - GitHub API

## Arquitectura

```text
+---------------------+
|       Cliente       |
|   Insomnia / curl   |
+----------+----------+
           |
           | HTTP GET
           | /api/github/me
           v
+---------------------+
|       FastAPI       |
|      API propia     |
+----------+----------+
           |
           | invoca
           v
+---------------------+
| github_service.py   |
|     HTTPX           |
+----------+----------+
           |
           | HTTPS
           | Bearer Token
           v
+---------------------+
|      GitHub API     |
|    /user endpoint   |
+----------+----------+
           |
           | JSON
           v
+---------------------+
|       FastAPI       |
+----------+----------+
           |
           | JSON
           v
+---------------------+
|       Cliente       |
+---------------------+

```