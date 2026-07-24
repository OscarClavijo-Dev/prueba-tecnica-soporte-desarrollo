# Implementación de Pressbooks

## Objetivo

Implementar Pressbooks como aplicación principal de la solución utilizando Docker Compose, respetando la arquitectura recomendada por la prueba técnica.

---

## ¿Qué es Pressbooks?

Pressbooks es una plataforma de publicación de libros digitales construida sobre WordPress.

Por esta razón requiere una base de datos compatible con MySQL/MariaDB y un entorno PHP para su funcionamiento.

---

## Componentes de la arquitectura

La implementación de Pressbooks utilizará una arquitectura multicontenedor.

Los componentes principales son:

- Pressbooks
- MariaDB
- Red Docker compartida
- Volúmenes persistentes

Cada servicio se ejecutará en un contenedor independiente y se comunicará mediante la red `backend` definida en Docker Compose.

Esta aproximación facilita el mantenimiento, la escalabilidad y el aislamiento de responsabilidades entre los distintos componentes.

## Arquitectura Inicial

Durante este Sprint se integrarán los siguientes componentes:

- Pressbooks
- MariaDB

Posteriormente se integrarán:

- PostgreSQL
- FastAPI
- API externa

---

## Selección del motor de base de datos

Aunque el proyecto ya dispone de PostgreSQL para la futura API propia, Pressbooks requiere una base de datos compatible con MySQL.

Por esta razón se incorporó un servicio MariaDB independiente.

Esta decisión permite mantener la compatibilidad con Pressbooks sin afectar la arquitectura planteada para los siguientes niveles de la prueba.


## Implementación de MariaDB

Se implementó un contenedor independiente para MariaDB como base de datos de Pressbooks.

### Decisiones tomadas

- Se utilizó la imagen oficial `mariadb:11`.
- Se definió un nombre explícito para el contenedor.
- Se configuró el reinicio automático mediante `restart: unless-stopped`.
- Se utilizaron variables de entorno para desacoplar la configuración.
- Se creó un volumen persistente (`mariadb_data`) para conservar la información.
- Se conectó el servicio a la red `backend`.

### Justificación

MariaDB será utilizada exclusivamente por Pressbooks, mientras que PostgreSQL permanecerá destinado a la API propia que se desarrollará en niveles posteriores.

### Beneficios

- Compatibilidad oficial con Pressbooks.
- Separación de responsabilidades.
- Arquitectura desacoplada.
- Posibilidad de reutilizar PostgreSQL para FastAPI.

## Decisiones Técnicas

Se decidió mantener PostgreSQL para la API propia y utilizar MariaDB únicamente para Pressbooks, respetando la arquitectura soportada oficialmente por la aplicación.