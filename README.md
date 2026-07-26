# Prueba Técnica - Soporte y Desarrollo

---

## Descripción

Este proyecto corresponde al desarrollo de la prueba técnica para el proceso
de selección del cargo de Soporte y Desarrollo.

La solución se construye progresivamente mediante una arquitectura basada en
contenedores Docker, una aplicación web, una API propia desarrollada con
FastAPI y una integración autenticada con una API externa.

Durante el desarrollo se priorizó:

- La organización del proyecto.
- La separación de responsabilidades.
- La documentación técnica.
- La protección de credenciales.
- La validación incremental de cada componente.
- El registro de problemas y soluciones.
- El control de versiones mediante Git.
- La posibilidad de ampliar la solución en etapas posteriores.

La implementación de Pressbooks fue investigada e intentada inicialmente.
Debido a las dificultades encontradas para disponer de un entorno funcional
dentro del alcance de la prueba, se utilizó WordPress como alternativa,
dejando documentada la estrategia para una futura incorporación de Pressbooks.

---

# Objetivo

Diseñar e implementar progresivamente una solución tecnológica que permita
demostrar capacidades de infraestructura, contenedores, integración de
servicios, consumo de APIs externas, procesamiento de información,
persistencia de datos y desarrollo de una API propia.

La solución se desarrolla siguiendo los niveles establecidos en la prueba
técnica y documentando tanto los componentes funcionales como las decisiones
y dificultades encontradas durante el proceso.

---

# Estado del proyecto

| Nivel | Estado |
|---|---|
| Nivel 1 - Preparación y Docker | ✅ Finalizado |
| Nivel 2 - Pressbooks / aplicación principal | ✅ Finalizado mediante alternativa documentada |
| Nivel 3 - Consumo de API externa | ✅ Finalizado |
| Nivel 4 - Procesamiento y almacenamiento | 🔄 Siguiente etapa |
| Nivel 5 - Desarrollo de API propia | 🔄 Base inicial implementada |
| Nivel 6 - Integración entre componentes | ⏳ Pendiente |
| Nivel 7 - Publicación | ⏳ Pendiente |
| Nivel 8 - Documentación y presentación | 🔄 En construcción |

---

# Arquitectura

## Arquitectura actual

```text
                         USUARIO
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       WORDPRESS :8080              FASTAPI :8000
              │                           │
              ▼                           ▼
         MARIADB 11                 GITHUB API
                                          │
                                          │ Bearer Token
                                          ▼
                                    GitHub /user

                                    

              POSTGRESQL :5433
                    ▲
                    │
                    │
              Nivel 4 - Persistencia

```

