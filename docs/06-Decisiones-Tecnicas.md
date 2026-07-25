# Decisiones Técnicas

## Implementación de Pressbooks

### Objetivo

La prueba técnica recomienda implementar Pressbooks utilizando Docker y Docker Compose.

### Investigación realizada

Antes de iniciar la implementación se revisó la documentación oficial del proyecto y se consultó la disponibilidad de imágenes Docker.

Durante la investigación se encontró que:

- Pressbooks no publica una imagen oficial en Docker Hub.
- La documentación oficial describe una instalación sobre un entorno PHP configurado, con múltiples dependencias del sistema.
- El proyecto requiere herramientas adicionales para la generación y exportación de libros (Ghostscript, ImageMagick, Poppler, Composer, entre otras).

### Intento realizado

Se preparó una infraestructura basada en Docker Compose utilizando MariaDB y una imagen oficial de WordPress.

Esta aproximación permitió validar:

- Comunicación entre contenedores.
- Persistencia mediante volúmenes.
- Variables de entorno.
- Redes Docker.
- Compatibilidad con la arquitectura requerida.

### Decisión adoptada

Debido a que no existe una imagen Docker oficial de Pressbooks y considerando el tiempo disponible para la prueba técnica, se decidió implementar WordPress como plataforma compatible.

Esta decisión está alineada con las condiciones establecidas en el documento de la prueba, el cual permite utilizar una aplicación alternativa siempre que se documenten las razones y la estrategia de integración futura.

### Integración futura

La arquitectura fue diseñada para permitir la sustitución del servicio WordPress por Pressbooks reutilizando:

- MariaDB.
- La red Docker.
- Los volúmenes persistentes.
- La configuración general de Docker Compose.

Esto reduciría significativamente el esfuerzo de migración.

## Justificación de la alternativa utilizada

El documento de la prueba permite implementar una aplicación alternativa cuando no sea posible desplegar Pressbooks, siempre que se expliquen las razones técnicas y el enfoque adoptado.

Durante el desarrollo se realizó una investigación de la documentación oficial y un intento de implementación. Se comprobó que Pressbooks no proporciona una imagen Docker oficial lista para usar y que su instalación requiere un entorno PHP configurado con dependencias adicionales.

Con el fin de entregar una solución funcional dentro del tiempo disponible, se implementó WordPress como plataforma compatible. Esta decisión permitió demostrar el despliegue mediante Docker Compose, la integración con MariaDB, la persistencia mediante volúmenes y la comunicación entre servicios.

La arquitectura diseñada facilita una futura sustitución del servicio WordPress por Pressbooks sin modificar la base de datos, la red ni la estructura general del proyecto.