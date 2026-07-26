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

| Tecnología | Uso |
|---|---|
| Docker Engine | Ejecución de contenedores |
| Docker Compose | Orquestación de servicios |
| PostgreSQL 17 | Base de datos de la API |
| MariaDB 11 | Base de datos de WordPress |
| WordPress | Alternativa temporal a Pressbooks |
| FastAPI | API propia |
| Python | Desarrollo de la API |
| HTTPX | Consumo de API externa |
| Git | Control de versiones |
| GitHub | Repositorio y API externa |
| Postman | Pruebas de API |

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
| 01-Arquitectura.md | Arquitectura general de la solución |
| 03-Errores.md | Errores encontrados y soluciones |
| 04-Instalacion.md | Instalación y configuración del entorno |
| 05-Pressbooks.md | Investigación e intento de implementación de Pressbooks |
| 06-Decisiones-Tecnicas.md | Decisiones técnicas y justificaciones |
| 07-Intento-Implementacion-Pressbooks.md | Evidencia del intento de implementación |
| 08-API-Externa.md | Planeación inicial de la integración externa |
| 09-FastAPI.md | Implementación y configuración de FastAPI |
| 10-API-Externa.md | Desarrollo de la integración con API externa |
| 11-Incidencias-fastapi.md | Incidencias encontradas durante la implementación de FastAPI |
| 12-API-GITHUB.md | Configuración e implementación de GitHub API |
| 13-Pruebas-API-GitHub.md | Evidencias de las pruebas de integración con GitHub |

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