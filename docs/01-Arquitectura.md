# Arquitectura

## Objetivo

    Definir una arquitectura basada en contenedores que permita ejecutar cada componente del proyecto de forma aislada, reproducible y fácilmente desplegable.

## Componentes

    Inicialmente la infraestructura estará compuesta por un único servicio:

    - PostgreSQL

    Este servicio servirá como base para comprender el funcionamiento de Docker Compose antes de incorporar componentes adicionales como Pressbooks, MariaDB y FastAPI.

## Validación de la infraestructura

    La infraestructura fue validada mediante los siguientes comandos:

    - `docker compose up -d`
    - `docker ps`
    - `docker logs postgres_db`
    - `docker volume ls`
    - `docker network ls`

    Se verificó la creación del contenedor PostgreSQL, el volumen persistente y la red dedicada utilizada por la solución.

## Contenedores

## Redes

## Volúmenes

## Variables de Entorno

    La infraestructura utiliza un archivo `.env` para desacoplar la configuración del código.

    Inicialmente se parametrizan:

    - Nombre de la base de datos
    - Usuario administrador
    - Contraseña inicial

Docker Compose inyecta estas variables automáticamente durante la creación del contenedor PostgreSQL.

## Decisiones Técnicas