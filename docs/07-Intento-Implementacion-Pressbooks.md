# Intento de Implementación de Pressbooks

## Objetivo

Implementar Pressbooks como aplicación principal utilizando Docker y Docker Compose, siguiendo las recomendaciones disponibles en la documentación oficial.

---

## Metodología

Se decidió realizar un intento de implementación antes de utilizar cualquier alternativa.

El objetivo fue identificar:

- Requisitos técnicos.
- Dependencias.
- Método oficial de instalación.
- Compatibilidad con Docker.
- Posibles dificultades durante el despliegue.

---

## Verificación de imágenes Docker

Se realizó una búsqueda de imágenes disponibles mediante Docker Hub.

Comando utilizado:

```bash
docker search pressbooks
```

Resultado:

NAME                                                    DESCRIPTION                                     STARS     OFFICIAL
guard13007/pressbooks-compatible-wordpress-dockerfile   Modifying the WordPress docker image to inst…   0         
bunmidavid/expressbooks2                                                                                0         

Observación:

Se verificará si existe una imagen oficial mantenida por el proyecto Pressbooks o si únicamente existen imágenes desarrolladas por terceros.