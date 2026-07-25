## Incidencia 1 - Selección de la imagen base

Durante la implementación se intentó utilizar la imagen:

wordpress:6.9.5-php8.3-apache

Docker respondió indicando que dicho tag no existía.

Después de revisar el repositorio oficial de imágenes de WordPress se identificó que la nomenclatura correcta utiliza el entorno de ejecución (PHP y Apache) como tag principal.

Imagen seleccionada finalmente:

wordpress:php8.3-apache

Esta decisión permite mantener compatibilidad con PHP 8.3, requerido por la documentación oficial de Pressbooks.