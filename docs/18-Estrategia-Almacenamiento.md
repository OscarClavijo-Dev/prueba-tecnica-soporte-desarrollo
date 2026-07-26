# Estrategia de Almacenamiento – Nivel 4

## 1. Base de datos seleccionada

Se selecciona PostgreSQL 17 como sistema de gestión de base de datos para la
persistencia de la información obtenida desde la API externa de GitHub.

La selección se fundamenta en:

- PostgreSQL ya forma parte de la infraestructura del proyecto.
- Es una base de datos relacional madura y ampliamente utilizada.
- Permite aplicar restricciones de integridad.
- Permite utilizar claves primarias y restricciones de unicidad.
- Permite trabajar con fechas y zonas horarias.
- Facilita la implementación de estrategias de sincronización.
- Permite demostrar claramente el modelo relacional solicitado en la prueba.

## 2. Arquitectura de almacenamiento

```text
GitHub API
    |
    | HTTPS + Bearer Token
    v
FastAPI
    |
    | Procesamiento de respuesta
    v
Servicio de sincronización
    |
    | SQLAlchemy
    v
PostgreSQL 17
    |
    v
github_users
``` 