## 1. Objetivo

El objetivo de esta etapa es integrar la aplicación principal basada en WordPress con la API REST desarrollada con FastAPI, permitiendo que WordPress consulte y presente información almacenada en la API propia.

La integración permite demostrar la comunicación entre:

1. WordPress como aplicación principal.
2. Un plugin personalizado desarrollado en PHP.
3. La API REST desarrollada con FastAPI.
4. PostgreSQL como sistema de persistencia.
5. Los datos obtenidos originalmente desde la API externa de GitHub.

La funcionalidad implementada permite consultar desde una página de WordPress los usuarios almacenados en la tabla `github_users` de PostgreSQL mediante el endpoint:

`GET /api/users`

---

## 2. Alcance

La integración implementada contempla:

- WordPress ejecutándose mediante Docker.
- FastAPI ejecutándose localmente mediante Uvicorn.
- PostgreSQL ejecutándose mediante Docker.
- Un plugin personalizado de WordPress.
- Un shortcode para insertar la vista en una página.
- Una llamada HTTP desde PHP hacia FastAPI.
- Procesamiento de la respuesta JSON.
- Renderización de los usuarios en WordPress.
- Visualización de nombre, login, correo electrónico y avatar.
- Enlaces hacia los perfiles de GitHub.
- Enlace directo para consultar el endpoint REST.
- Manejo básico de errores HTTP y respuestas inválidas.

---

## 3. Arquitectura de la integración

La arquitectura implementada está compuesta por los siguientes componentes:

| Componente | Tecnología | Responsabilidad |
|---|---|---|
| Aplicación principal | WordPress | Presentar la información al usuario |
| Plugin de integración | PHP | Realizar la llamada HTTP a FastAPI |
| API propia | FastAPI | Exponer los usuarios almacenados |
| Persistencia | PostgreSQL | Almacenar los usuarios |
| Contenedores | Docker | Ejecutar WordPress y PostgreSQL |
| Servidor API | Uvicorn | Ejecutar FastAPI |
| API externa | GitHub API | Fuente original de información |

---

## 4. Flujo general

El flujo de integración es:

```text
Usuario
   |
   v
WordPress
   |
   v
Página "Usuarios GitHub"
   |
   v
Shortcode [github_users]
   |
   v
Plugin GitHub Users
   |
   | HTTP GET
   v
FastAPI
   |
   v
GET /api/users
   |
   v
PostgreSQL
   |
   v
JSON
   |
   v
Plugin WordPress
   |
   v
HTML
   |
   v
Usuario
```

## 5. Plugin de integración

El plugin está ubicado en:

wordpress-plugin/github-users/

Su estructura es:

```text
wordpress-plugin/
└── github-users/
    ├── github-users.php
    └── assets/
        └── css/
            └── github-users.css
```
## 5.1 Archivo principal

El archivo principal es:


```text
wordpress-plugin/github-users/github-users.php
```

Este archivo contiene:

* Cabecera del plugin.
* Carga de estilos.
* Shortcode.
* Llamada HTTP a la API.
* Validación de la respuesta.
* Decodificación JSON.
* Renderización HTML.
* Escape de valores.
* Enlaces hacia GitHub.
* Enlace hacia la API REST.

## 6. Shortcode

El plugin registra el siguiente shortcode:
```text
[github_users]
```

Este shortcode permite insertar la integración en cualquier página o contenido compatible de WordPress.

Por ejemplo:
```text
Usuarios GitHub

[github_users]
```

Cuando WordPress procesa la página, ejecuta la función asociada al shortcode y genera dinámicamente la vista.

## 7. Consulta de la API REST

El plugin realiza una petición HTTP mediante wp_remote_get().

El endpoint utilizado es:

```text
http://host.docker.internal:8000/api/users
```

La llamada utiliza:

```text
$response = wp_remote_get(
    $api_url,
    array(
        'timeout' => 10,
        'headers' => array(
            'Accept' => 'application/json',
        ),
    )
);
```

El timeout evita que WordPress quede esperando indefinidamente si la API no responde.

## 8. Comunicación entre Docker y el host

WordPress se ejecuta dentro del contenedor:

```text
wordpress_app
```

Mientras que FastAPI se ejecuta en el sistema anfitrión mediante Uvicorn.

FastAPI está escuchando en:

```text
127.0.0.1:8000
```

Para permitir que el contenedor de WordPress acceda al servicio del equipo anfitrión se utiliza:

```text
host.docker.internal
```

Por esta razón el plugin utiliza:

```text
http://host.docker.internal:8000/api/users
```

En lugar de:
```text
http://127.0.0.1:8000/api/users
```

Dentro de un contenedor, 127.0.0.1 representa al propio contenedor y no al sistema anfitrión.

## 9. Validación de la respuesta

El plugin valida si la petición produjo un error:

```text
if (is_wp_error($response)) {
    ...
}
```

También valida el código HTTP:
```text
$status_code = wp_remote_retrieve_response_code($response);

if ($status_code !== 200) {
    ...
}

```

Finalmente obtiene el cuerpo:
```text
$body = wp_remote_retrieve_body($response);
```
Y transforma el JSON en un arreglo PHP:
```text
$users = json_decode($body, true);
```
Se valida que la respuesta sea un arreglo:
```text
if (!is_array($users)) {
    ...
}
```
También se contempla el caso de que no existan usuarios.

## 10. Información presentada

La vista de WordPress presenta información proveniente directamente de la API propia.

Para cada usuario se muestran:

Login de GitHub.
Nombre.
Correo electrónico.
Avatar.
Enlace hacia el perfil de GitHub.

Cuando un campo opcional no existe, se muestra un valor alternativo.

Por ejemplo:

Sin nombre

o:

Sin email

Esto permite que la interfaz siga funcionando aunque la API entregue campos null.

## 11. Seguridad básica en la salida HTML

Los datos recibidos desde la API no se insertan directamente en el HTML.

Se utilizan funciones de escape de WordPress:
```text
esc_html()
esc_attr()
esc_url()
```
Por ejemplo:
```text
esc_html($login)
```
y:
```text
esc_url($avatar_url)
```
Esto reduce riesgos relacionados con la inserción de contenido no confiable en la salida HTML.

## 12. Enlace directo hacia la API

La vista incluye un enlace:
```text
Consultar API REST
```
Este enlace permite abrir directamente:
```text
GET /api/users
```
desde el navegador.

La finalidad es permitir comprobar que la información presentada por WordPress corresponde con la respuesta de la API.

## 13. Enlaces hacia GitHub

Cada usuario puede incluir un enlace:

Ver perfil en GitHub

El enlace utiliza el valor html_url recibido desde la API.

Se abre en una nueva pestaña utilizando:
```text
target="_blank"
rel="noopener noreferrer"
```

## 14. Estilos

El plugin carga el archivo:
```text
wordpress-plugin/github-users/assets/css/github-users.css
```
Los estilos proporcionan:

* Tarjetas de usuarios.
* Distribución mediante grid.
* Avatar.
* Información del usuario.
* Botones.
* Mensajes de error.
* Diseño adaptable.

## 15. Página de WordPress

La integración se presenta en una página de WordPress destinada a consultar los usuarios.

La página contiene el shortcode:
```text
[github_users]
```
Al acceder a la página, WordPress ejecuta el plugin y obtiene la información de FastAPI.

La vista generada muestra los usuarios almacenados en la API.

## 16. Levantamiento de los componentes

### 16.1 PostgreSQL

PostgreSQL se ejecuta mediante Docker.

Contenedor:
```text
postgres_db
```
Puerto publicado:
```text
5433 -> 5432
```
Comprobación:

docker ps

Resultado esperado:
```text
postgres_db   postgres:17   0.0.0.0:5433->5432/tcp
16.2 WordPress
```
WordPress se ejecuta mediante Docker.

Contenedor:
```text
wordpress_app
```
Puerto:
```text
8080 -> 80
```
La aplicación se consulta desde:
```text
http://127.0.0.1:8080
16.3 FastAPI
```
FastAPI se ejecuta desde el entorno virtual del proyecto.

Ejemplo:
```text
source .venv/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
La API queda disponible en:
```text
http://127.0.0.1:8000
```

## 17. Verificación de la API

Se comprobó que el endpoint:
```text
GET /api/users
```
responde correctamente.

Prueba:
```text
curl --max-time 10 -s -o /tmp/api-users.json \
  -w "HTTP_STATUS=%{http_code}\n" \
  http://127.0.0.1:8000/api/users
```
Resultado:
```text
HTTP_STATUS=200
```
## 18. Verificación desde el contenedor de WordPress

Se comprobó que WordPress puede acceder a FastAPI:
```text
docker exec wordpress_app curl --max-time 10 -s \
  -o /tmp/api-users.json \
  -w "HTTP_STATUS=%{http_code}\n" \
  http://host.docker.internal:8000/api/users
```
Resultado:
```text
HTTP_STATUS=200
```
Esta prueba es importante porque valida la comunicación real entre los dos componentes.

## 19. Verificación del plugin

Se comprobó la sintaxis PHP:
```text
php -l wordpress-plugin/github-users/github-users.php
```
Resultado:
```text
No syntax errors detected in wordpress-plugin/github-users/github-users.php
```
También se verificó dentro del contenedor:
```text
docker exec wordpress_app php -l \
  /var/www/html/wp-content/plugins/github-users/github-users.php
```
Resultado:

No syntax errors detected

## 20. Verificación de los archivos del plugin

Se verificaron los archivos dentro del contenedor:
```text
docker exec wordpress_app sh -c \
'ls -lh /var/www/html/wp-content/plugins/github-users/github-users.php \
/var/www/html/wp-content/plugins/github-users/assets/css/github-users.css'
```
Los archivos fueron encontrados correctamente.

## 21. Verificación de WordPress

Se comprobó que WordPress responde correctamente:
```text
curl --max-time 10 -s \
  -o /tmp/wordpress.html \
  -w "HTTP_STATUS=%{http_code}\n" \
  http://127.0.0.1:8080/?page_id=5
```
Resultado:
```text
HTTP_STATUS=200
```
También se verificó que la página contiene información proveniente de la API:
```text
grep -o "OscarClavijo-Dev" /tmp/wordpress.html | head
```
Resultado:

OscarClavijo-Dev
OscarClavijo-Dev
OscarClavijo-Dev

Esto demuestra que WordPress procesó el shortcode y presentó los datos obtenidos desde FastAPI.

## 22. Resultado visual

La página de WordPress presenta una vista denominada:

Usuarios GitHub

La vista muestra las tarjetas correspondientes a los usuarios almacenados.

Cada tarjeta presenta la información recibida desde:

```text
GET /api/users
```
La vista fue validada visualmente desde el navegador.

## 23. Resultado de la integración

La integración permite realizar el siguiente recorrido:

```text
PostgreSQL
     |
     v
FastAPI
     |
     | GET /api/users
     v
Plugin WordPress
     |
     v
Shortcode
     |
     v
Página WordPress
     |
     v
Usuario
```

La integración es funcional y permite consultar información real de la API propia desde la aplicación principal.

## 24. Cumplimiento del Nivel 6

La implementación cumple los ejemplos de integración propuestos:

Requisito	Cumplimiento
Mostrar en WordPress información obtenida desde la API propia	✅
Crear una página o bloque que consulte datos almacenados	✅
Utilizar plugin, shortcode, módulo o llamada HTTP	✅
Crear una vista sencilla para consultar datos	✅
Agregar enlaces entre WordPress y la API	✅
Documentar el proceso de integración	✅

También se cumple la modalidad de entrega parcial aceptada mediante:

* Prototipo funcional.
* Página de WordPress.
* Capturas de pantalla.
* Diagrama de arquitectura/flujo.
* Integración real.
* Explicación técnica del flujo.

## 25. Conclusión

El Nivel 6 queda implementado mediante una integración funcional entre WordPress y la API REST propia.

WordPress actúa como aplicación principal y utiliza un plugin personalizado para realizar una llamada HTTP a FastAPI. FastAPI consulta PostgreSQL y devuelve los usuarios almacenados en formato JSON. El plugin procesa la respuesta y genera una vista HTML dentro de WordPress.

De esta manera se demuestra una integración real entre la aplicación principal, la API propia y los datos persistidos.