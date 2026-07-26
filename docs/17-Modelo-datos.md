# Modelo de Datos – Nivel 4

## 1. Objetivo

El objetivo del modelo de datos es definir la estructura relacional utilizada para almacenar la información obtenida desde la API externa de GitHub.

La solución utiliza PostgreSQL 17, incorporado a la infraestructura del proyecto mediante Docker Compose.

El modelo persiste la información correspondiente al usuario autenticado obtenido mediante:

`GET https://api.github.com/user`

La información es procesada por FastAPI y posteriormente almacenada en PostgreSQL mediante una estrategia de sincronización.

---

## 2. Entidad principal

La entidad persistida es:

`github_users`

Representa los usuarios obtenidos desde GitHub que han sido procesados por la aplicación y almacenados localmente.

No se incorporan entidades adicionales que no estén justificadas por los requisitos actuales de la prueba técnica.

---

## 3. Estructura

| Campo | Tipo PostgreSQL | Restricciones | Descripción |
|---|---|---|---|
| id | BIGINT | PK, NOT NULL | Identificador interno del registro |
| github_id | BIGINT | NOT NULL, UNIQUE | Identificador único del usuario en GitHub |
| login | VARCHAR(255) | NOT NULL | Nombre de usuario de GitHub |
| name | VARCHAR(255) | NULL | Nombre público del usuario |
| email | VARCHAR(320) | NULL | Correo electrónico, si GitHub lo proporciona |
| avatar_url | TEXT | NULL | URL del avatar del usuario |
| html_url | TEXT | NULL | URL del perfil público de GitHub |
| created_at | TIMESTAMPTZ | NOT NULL | Fecha de creación del registro local |
| updated_at | TIMESTAMPTZ | NOT NULL | Fecha de última actualización del registro local |

---

## 4. Claves y restricciones

### Primary Key

`id` funciona como identificador interno de la entidad.

Se mantiene separado de `github_id` para desacoplar el modelo interno del identificador proporcionado por el sistema externo.

### Identificador externo

`github_id` almacena el identificador original proporcionado por GitHub.

La restricción `UNIQUE` evita que un mismo usuario externo sea almacenado más de una vez.

Esta restricción complementa la lógica de sincronización implementada en la aplicación.

### Campos opcionales

`name` y `email` permiten valores `NULL`, debido a que la API de GitHub puede no proporcionar estos datos.

---

## 5. Índices

El modelo cuenta con un índice asociado a la restricción `UNIQUE`
establecida sobre `github_id`.

Esta restricción permite:

- Evitar registros duplicados del mismo usuario de GitHub.
- Optimizar las búsquedas por el identificador externo.
- Servir como soporte para la estrategia de sincronización mediante
  operaciones de inserción y actualización.

No se crean índices adicionales sobre `login` o `updated_at` en esta etapa,
debido a que el volumen actual de datos es reducido y no existe todavía una
necesidad demostrada de optimizar dichas consultas.

Si el volumen de información aumenta o aparecen consultas frecuentes por
estos campos, se podrá incorporar índices adicionales mediante una nueva
migración.

## 6. Normalización

El modelo inicial contiene una única entidad porque el requisito actual se limita a persistir la información del usuario autenticado.

No se crean tablas artificiales para incrementar la complejidad del modelo.

La información almacenada representa un único concepto y no contiene grupos repetitivos ni relaciones que requieran descomposición en entidades adicionales.

---

## 7. Identificador interno frente a identificador externo

Se utilizan dos identificadores con responsabilidades diferentes:

```text
id
└── Identificador interno de PostgreSQL

github_id
└── Identificador proveniente de GitHub
```