# Estrategia de Almacenamiento – Nivel 4

## 1. Objetivo

La estrategia de almacenamiento define cómo la información obtenida desde la
API externa de GitHub es procesada, identificada, almacenada y posteriormente
actualizada en la base de datos.

Para esta etapa se utiliza PostgreSQL 17 como sistema de gestión de base de
datos relacional.

El objetivo no es almacenar indiscriminadamente toda la respuesta JSON
recibida desde GitHub, sino seleccionar y persistir los atributos necesarios
para representar al usuario externo dentro del modelo de datos de la
aplicación.

---

## 2. Base de datos seleccionada

Se selecciona PostgreSQL 17 como sistema de almacenamiento por las siguientes
razones:

- PostgreSQL ya forma parte de la infraestructura del proyecto.
- Es una base de datos relacional madura y ampliamente utilizada.
- Permite definir claves primarias y restricciones de integridad.
- Permite utilizar restricciones `UNIQUE` para evitar registros duplicados.
- Permite trabajar con tipos de datos adecuados para identificadores,
  cadenas de texto y fechas.
- Permite almacenar fechas con información de zona horaria mediante
  `TIMESTAMPTZ`.
- Facilita operaciones de inserción y actualización.
- Permite implementar estrategias de sincronización entre una API externa y
  la base de datos local.
- Permite demostrar claramente el modelo relacional solicitado en la prueba
  técnica.

La base de datos PostgreSQL se ejecuta mediante Docker Compose.

---

## 3. Arquitectura de almacenamiento

El flujo implementado es:

```text
GitHub API
    |
    | HTTPS + Bearer Token
    v
FastAPI
    |
    | Respuesta JSON
    v
GitHub Sync Service
    |
    | Selección y transformación
    | de los campos necesarios
    v
SQLAlchemy ORM
    |
    | INSERT / UPDATE
    v
PostgreSQL 17
    |
    v
github_users

``` 