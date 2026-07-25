# Consumo de API Externa

## API seleccionada

GitHub REST API

## Motivo de selección

## Tipo de autenticación

Bearer Token (Personal Access Token)

## Configuración de credenciales

Se utiliza una variable de entorno (`GITHUB_TOKEN`) para evitar exponer información sensible en el código fuente.

## Endpoint consumido

GET /user

## Validaciones implementadas

- Token inválido.
- Error de conexión.
- Respuesta vacía.
- Límite de peticiones (Rate Limit).

## Evidencias

- Captura en Postman.
- Respuesta JSON.
- Colección Postman exportada.