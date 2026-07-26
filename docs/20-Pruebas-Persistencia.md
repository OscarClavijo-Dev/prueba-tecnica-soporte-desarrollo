# Pruebas de Persistencia – Nivel 4

## 1. Objetivo

Validar que la información obtenida desde la API externa de GitHub pueda ser
almacenada correctamente en PostgreSQL y que la estrategia de sincronización
evite registros duplicados.

## 2. Pruebas realizadas

### 2.1 Creación de tabla

Se verificó la existencia de la tabla:

```text
github_users
```