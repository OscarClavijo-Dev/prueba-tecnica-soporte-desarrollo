# Migraciones PostgreSQL – Nivel 4

## 1. Objetivo

Las migraciones permiten definir de forma reproducible la estructura de la
base de datos utilizada por la aplicación.

Para este proyecto se utiliza inicialmente un script SQL versionado dentro
del repositorio.

La migración correspondiente al modelo de usuarios de GitHub se encuentra en:

`app/database/migrations/001_create_github_users.sql`

## 2. Migración inicial

Archivo:

```text
app/database/migrations/001_create_github_users.sql