# Integración con API externa

## Objetivo

Integrar una API externa autenticada como parte del Nivel 3 de la prueba técnica.

## API seleccionada

GitHub API.

## Método de autenticación

Bearer Token.

## Gestión de credenciales

La credencial se almacenará mediante una variable de entorno definida en `.env`.

El archivo `.env` está excluido del control de versiones mediante `.gitignore`.

Se proporciona `.env.example` como plantilla para configurar el entorno.

## Gestión de configuración

La configuración sensible de la integración con la API externa se gestiona mediante variables de entorno.

Se utiliza `pydantic-settings` para cargar la configuración desde el archivo `.env`.

La aplicación utiliza una clase de configuración centralizada para acceder a las variables necesarias sin incluir credenciales directamente en el código fuente.

El archivo `.env` se encuentra excluido del control de versiones mediante `.gitignore`.

El repositorio incluye `.env.example` como plantilla para facilitar la configuración de un nuevo entorno.

## Dependencias

Para la gestión de configuración se agregó:

- pydantic-settings
- python-dotenv

Las dependencias se registran en `requirements.txt`.

## Problema: ModuleNotFoundError al ejecutar prueba de GitHub

### Descripción

### ModuleNotFoundError al ejecutar prueba de GitHub

Durante la ejecución inicial del script de validación de GitHub se produjo
un `ModuleNotFoundError` debido a la forma en que Python resolvía los
imports al ejecutar directamente el archivo.

La solución fue ejecutar el script como módulo desde la raíz:

```bash
python -m scripts.test_github







