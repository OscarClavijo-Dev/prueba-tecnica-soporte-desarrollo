# Prueba Técnica - Soporte y Desarrollo

## Descripción

## Objetivo

## Arquitectura

### Arquitectura inicial

    La infraestructura del proyecto se construirá de manera incremental.

    El primer servicio implementado será PostgreSQL mediante Docker Compose. Posteriormente se integrarán MariaDB, Pressbooks y FastAPI sobre la misma infraestructura.

## Tecnologías

| Tecnología | Propósito |
|------------|-----------|
| Git | Control de versiones del proyecto. |
| GitHub | Hospedaje del repositorio y colaboración. |
| Docker | Contenerización de la solución. |
| Docker Compose | Orquestación de los servicios. |
| Pressbooks | Aplicación principal solicitada por la prueba. |
| MariaDB | Base de datos utilizada por Pressbooks. |
| PostgreSQL | Base de datos para la API propia. |
| FastAPI | Framework para desarrollar la API REST. |
| Postman | Pruebas de los endpoints. |
| VS Code | Entorno de desarrollo. |
| Fedora 44 | Sistema operativo de desarrollo. |

## Requisitos

## Entorno de desarrollo

    El proyecto fue desarrollado sobre el siguiente entorno:

    | Componente | Versión |
    |------------|----------|
    | Sistema Operativo | Fedora 44 |
    | Editor | Visual Studio Code |
    | Control de versiones | Git |
    | Contenedores | Docker CE  |
    | Orquestación | Docker Compose |

    El proyecto fue desarrollado sobre Fedora 44 utilizando Docker como plataforma de contenedores.

### Componentes instalados

    - Docker Engine
    - Docker CLI
    - Docker Compose
    - Docker Desktop

    Docker Desktop se emplea únicamente como herramienta gráfica para administrar los recursos del proyecto durante el desarrollo.

## Herramientas utilizadas

Además del motor de Docker se instaló Docker Desktop para facilitar la administración gráfica de contenedores, imágenes, redes y volúmenes durante el desarrollo y las pruebas del proyecto.

## Instalación

## Variables de Entorno

    El proyecto utiliza un archivo `.env` para almacenar la configuración sensible y facilitar la parametrización del entorno.

    Actualmente se definen las credenciales iniciales de PostgreSQL mediante variables de entorno consumidas por Docker Compose.

## Estado actual del proyecto

Actualmente el proyecto cuenta con una infraestructura base implementada mediante Docker Compose.

Componentes disponibles:

- PostgreSQL 17
- Docker Network (`backend`)
- Docker Volume (`postgres_data`)
- Variables de entorno mediante `.env`

Esta infraestructura servirá como base para integrar Pressbooks y los demás componentes solicitados en la prueba técnica.


## Estructura del proyecto

## Docker

## API externa

## Base de Datos

## API Propia

## PressBooks

## Evidencias

## Problemas encontrados

## Decisiones técnicas

   <p> Fedora incluye Podman como solución nativa para contenedores. Sin embargo, se decidió utilizar Docker debido a <br>que la prueba técnica lo solicita explícitamente y es ampliamente utilizado en entornos empresariales.</p>

## Mejoras futuras

## Autor