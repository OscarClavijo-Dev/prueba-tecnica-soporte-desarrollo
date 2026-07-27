## 1. Objetivo

Este documento describe detalladamente el flujo técnico de integración entre WordPress, el plugin personalizado, FastAPI y PostgreSQL.

La finalidad es explicar cómo una solicitud realizada desde una página de WordPress termina obteniendo información almacenada en la base de datos y cómo dicha información vuelve a WordPress para ser presentada al usuario.

---

## 2. Componentes

La integración está formada por:

```text
Usuario
   |
   v
WordPress
   |
   v
Plugin GitHub Users
   |
   v
FastAPI
   |
   v
PostgreSQL
```

Además, GitHub representa la fuente externa original de los datos almacenados.

## 3. Flujo de datos

El flujo completo es:
```text
GitHub API
    |
    | información de usuarios
    v
FastAPI
    |
    | almacenamiento
    v
PostgreSQL
    |
    | consulta
    v
GET /api/users
    |
    | JSON
    v
Plugin WordPress
    |
    | procesamiento PHP
    v
Shortcode [github_users]
    |
    v
Página WordPress
    |
    v
Usuario
```

## 4. Paso 1 - Usuario accede a WordPress

El usuario accede a WordPress mediante:
```text
http://127.0.0.1:8080
```
Posteriormente accede a la página de usuarios.

La página contiene:
```text
[github_users]
```
Este shortcode activa la lógica del plugin.

## 5. Paso 2 - WordPress ejecuta el shortcode

WordPress detecta:
```text
[github_users]
```
y ejecuta:
```text
github_users_shortcode()
```
La función se encarga de solicitar la información a FastAPI.

## 6. Paso 3 - Plugin realiza la llamada HTTP

El plugin define:
```text
http://host.docker.internal:8000/api/users
```
y realiza:
```text
GET /api/users
```
mediante:
```text
wp_remote_get()
```

## 7. Paso 4 - Comunicación Docker / Host

WordPress está dentro de Docker.

FastAPI está ejecutándose en el sistema anfitrión.

Por eso no se utiliza:
```text
127.0.0.1:8000
```
desde WordPress.

Se utiliza:
```text
host.docker.internal:8000
```
Esta dirección permite que el contenedor de WordPress alcance el servicio que está ejecutándose en el equipo anfitrión.

## 8. Paso 5 - FastAPI recibe la petición

FastAPI recibe:
```text
GET /api/users
```
El router correspondiente procesa la solicitud.

El endpoint devuelve los usuarios almacenados.

## 9. Paso 6 - Consulta PostgreSQL

La API consulta la información almacenada en PostgreSQL.

La tabla principal involucrada es:
```text
github_users
```
La información puede incluir:

* id
* github_id
* login
* name
* email
* avatar_url
* html_url
* created_at
* updated_at

## 10. Paso 7 - FastAPI devuelve JSON

FastAPI transforma los registros en una respuesta JSON.

Ejemplo simplificado:
```text
[
    {
        "login": "OscarClavijo-Dev",
        "name": null,
        "email": null,
        "avatar_url": "https://avatars.githubusercontent.com/...",
        "html_url": "https://github.com/OscarClavijo-Dev"
    }
]
```
## 11. Paso 8 - WordPress recibe la respuesta

El plugin obtiene el contenido:
```text
$body = wp_remote_retrieve_body($response);
```
Después convierte JSON a arreglo PHP:
```text
$users = json_decode($body, true);
```
## 12. Paso 9 - Validación

El plugin verifica:

- Que no exista un error de conexión.
- Que la API responda HTTP 200.
- Que la respuesta tenga formato JSON válido.
- Que exista un arreglo de usuarios.
- Que existan registros para mostrar.

Si alguna condición falla, se presenta un mensaje controlado.

## 13. Paso 10 - Renderización

Por cada usuario se genera una tarjeta HTML.

La tarjeta incluye:

- Avatar
- Login
- Nombre
- Email
- Perfil de GitHub

Los datos son escapados utilizando funciones de WordPress.

## 14. Paso 11 - Presentación

El HTML generado por el plugin se incorpora a la página de WordPress.

El navegador presenta finalmente:

Usuarios GitHub

+------------------+
| Avatar           |
| Login            |
| Nombre           |
| Email            |
| Ver perfil GitHub|
+------------------+

## 15. Enlace "Consultar API REST"

La página también contiene:
```text
Consultar API REST
```
Este enlace permite verificar directamente la respuesta de:
```text
GET /api/users
```
Su finalidad es facilitar la comprobación de que los datos que WordPress presenta proceden realmente de la API.

## 16. Flujo completo con responsabilidades

Etapa	Componente	Responsabilidad
1	Usuario	Solicitar la página
2	WordPress	Procesar la página
3	Shortcode	Activar el plugin
4	Plugin PHP	Realizar la llamada HTTP
5	FastAPI	Procesar endpoint
6	PostgreSQL	Proporcionar datos persistidos
7	FastAPI	Serializar datos a JSON
8	Plugin	Procesar JSON
9	WordPress	Generar HTML
10	Navegador	Mostrar información

## 17. Diagrama de secuencia

Usuario          WordPress       Plugin        FastAPI       PostgreSQL
  |                 |              |             |               |
  |-- Solicitud --->|              |             |               |
  |                 |              |             |               |
  |                 |-- shortcode->|             |               |
  |                 |              |             |               |
  |                 |              |-- GET ----->|               |
  |                 |              |             |-- SELECT ---->|
  |                 |              |             |<-- registros -|
  |                 |              |<-- JSON -----|               |
  |                 |<-- HTML ------|             |               |
  |<-- Página ------|              |             |               |
  |                 |              |             |               |

## 18. Comunicación entre servicios

En el entorno local se tienen los siguientes componentes:
```text
WordPress
127.0.0.1:8080
       |
       | host.docker.internal:8000
       v
FastAPI
127.0.0.1:8000
       |
       v
PostgreSQL
5433 -> 5432
```
## 19. Dependencias

La integración depende de que estén disponibles:

Docker.
Contenedor WordPress.
Contenedor PostgreSQL.
Python.
Entorno virtual .venv.
Dependencias Python instaladas.
FastAPI.
Uvicorn.
Base de datos inicializada.
Plugin instalado.
Página de WordPress con shortcode.

## 20. Consideración importante para ejecución local

La URL:
```text
host.docker.internal
```
se utiliza para el entorno local definido en esta prueba técnica.

No debe interpretarse como una URL pública.

Para un despliegue productivo, la dirección de la API debería configurarse mediante una variable de entorno o configuración externa.

## 21. Resultado

El flujo demuestra una integración entre:

Aplicación principal
       +
Plugin
       +
API propia
       +
Persistencia

Esto satisface el objetivo del Nivel 6 de integrar los diferentes componentes desarrollados durante la prueba.