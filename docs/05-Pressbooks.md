# Implementación de Pressbooks

## Objetivo

Implementar Pressbooks como aplicación principal de la solución utilizando Docker Compose, respetando la arquitectura recomendada por la prueba técnica.

---

## ¿Qué es Pressbooks?

Pressbooks es una plataforma de publicación de libros digitales construida sobre WordPress.

Por esta razón requiere una base de datos compatible con MySQL/MariaDB y un entorno PHP para su funcionamiento.

---

## Arquitectura Inicial

Durante este Sprint se integrarán los siguientes componentes:

- Pressbooks
- MariaDB

Posteriormente se integrarán:

- PostgreSQL
- FastAPI
- API externa

---

## Decisiones Técnicas

Se decidió mantener PostgreSQL para la API propia y utilizar MariaDB únicamente para Pressbooks, respetando la arquitectura soportada oficialmente por la aplicación.