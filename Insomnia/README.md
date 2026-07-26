# Pruebas de API mediante Insomnia

## Motivo de utilización

Inicialmente se contempló utilizar Postman para las pruebas de la API.

Durante el desarrollo sobre Fedora 44 se presentaron dificultades con el
funcionamiento de Postman en el entorno utilizado.

Como alternativa se seleccionó Insomnia.

La decisión no modifica la arquitectura ni la implementación de la API,
ya que Insomnia únicamente actúa como cliente para realizar pruebas HTTP.

## Pruebas realizadas

### Prueba 1 - Usuario autenticado

Solicitud:

GET /api/github/me

Resultado esperado:

HTTP 200 OK

La respuesta contiene la información del usuario autenticado en GitHub.

### Prueba 2 - Ruta inexistente

Solicitud:

GET /api/github/no-existe

Resultado esperado:

HTTP 404 Not Found

### Prueba 3 - API externa

Solicitud:

GET https://api.github.com/user

La solicitud utiliza:

- Bearer Token
- Accept
- GitHub API Version

## Evidencias

Las capturas de las solicitudes y respuestas se almacenarán en:

docs/evidencias/nivel-3/

## Resultado

Las pruebas permitieron validar tanto la API propia como la comunicación
con el servicio externo.