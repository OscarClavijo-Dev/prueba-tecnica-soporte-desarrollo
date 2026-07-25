# Prueba Técnica - Soporte y Desarrollo

---

# Descripción

Este proyecto corresponde al desarrollo de la prueba técnica para el proceso de selección del cargo de Soporte y Desarrollo.

La solución fue diseñada utilizando una arquitectura basada en contenedores Docker, permitiendo desacoplar los diferentes servicios y facilitar su despliegue, mantenimiento y escalabilidad.

Durante el desarrollo se priorizó la documentación de cada decisión técnica, la validación incremental de los componentes y el uso de buenas prácticas de infraestructura.

Breve descripción del proyecto.

---

## Objetivo

Diseñar e implementar una infraestructura basada en Docker Compose que permita desplegar los componentes solicitados por la prueba técnica, documentando cada fase del proceso, las decisiones tomadas y las posibles alternativas de implementación cuando existan limitaciones técnicas.
---

## Estado del proyecto

|| Nivel | Estado |
|--------|--------|
| Nivel 1 | ✅ Finalizado |
| Nivel 2 | ✅ Finalizado |
| Nivel 3 | 🟡 Configuración inicial completada |
| Nivel 4 | ⏳ Pendiente |
| Nivel 5 | ⏳ Pendiente |

---

# Arquitectura



```text
                Usuario
                    │
                    ▼
             WordPress (Temporal)
                    │
                    ▼
               MariaDB 11
                    │
                    ▼
               FastAPI (Pendiente)
                    │
                    ▼
             PostgreSQL 17
                    │
                    ▼
              API Externa
```

La arquitectura fue diseñada para permitir reemplazar posteriormente WordPress por Pressbooks reutilizando la infraestructura existente.

# Tecnologías utilizadas

(| Tecnología     | Uso                      |
| -------------- | ------------------------ |
| Docker Engine  | Contenedores             |
| Docker Compose | Orquestación             |
| Docker Desktop | Administración           |
| PostgreSQL 17  | Base de datos API        |
| MariaDB 11     | Base de datos Pressbooks |
| WordPress      | Plataforma temporal      |
| FastAPI        | API propia (pendiente)   |
| Git            | Versionamiento           |
| GitHub         | Repositorio              |


---

## Componentes implementados

- ✅ Docker Engine
- ✅ Docker Compose
- ✅ Docker Desktop
- ✅ PostgreSQL
- ✅ MariaDB
- ✅ WordPress (Infraestructura preparada)
- ✅ Entorno virtual Python (.venv)
- ✅ Dependencias iniciales de FastAPI
- ✅ requirements.txt

## Documentación

| Documento | Descripción |
|------------|-------------|
| 01-Configuracion-Git.md | Configuración inicial del repositorio |
| 02-Docker.md | Instalación de Docker |
| 03-PostgreSQL.md | Configuración de PostgreSQL |
| 04-Entorno.md | Configuración del entorno |
| 05-Pressbooks.md | Investigación e implementación |
| 06-Decisiones-Tecnicas.md | Justificación de las decisiones |
| 07-Intento-Implementacion-Pressbooks.md | Evidencia del intento de implementación |

# Evidencias

Capturas

Logs

Resultados

---

# Problemas encontrados

Aquí iremos agregando cada problema solucionado.

---

## Decisiones técnicas

La implementación de Pressbooks se investigó siguiendo la documentación oficial.

Durante el proceso se identificó que el proyecto no distribuye una imagen Docker oficial y que su instalación requiere un entorno PHP con múltiples dependencias adicionales.

Debido al tiempo disponible para la prueba y conforme a las condiciones establecidas en el documento de evaluación, se preparó una infraestructura compatible utilizando WordPress, documentando el proceso y la estrategia para una futura migración hacia Pressbooks.

La explicación completa se encuentra en:

docs/06-Decisiones-Tecnicas.md

# Mejoras futuras

- Implementar Pressbooks sobre la infraestructura existente.
- Desarrollar la API propia con FastAPI.
- Integrar la API externa solicitada.
- Incorporar pruebas automatizadas.
- Implementar CI/CD.
---

# Autor