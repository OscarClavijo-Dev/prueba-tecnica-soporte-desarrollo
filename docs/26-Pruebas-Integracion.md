## 1. Objetivo

Este documento registra las pruebas realizadas para validar la integración entre WordPress y la API REST desarrollada con FastAPI.

Las pruebas buscan comprobar:

- Disponibilidad de FastAPI.
- Funcionamiento del endpoint `/api/users`.
- Acceso desde el contenedor WordPress.
- Sintaxis correcta del plugin PHP.
- Presencia de los archivos del plugin.
- Respuesta HTTP de WordPress.
- Renderización de datos provenientes de la API.
- Funcionamiento de los enlaces de integración.

---

# 2. Prerrequisitos

Antes de realizar las pruebas se deben tener disponibles:

```text
Docker
Python
FastAPI
Uvicorn
PostgreSQL
WordPress
Plugin GitHub Users
```

# 3. Estado de los contenedores

Se verificó el estado de los contenedores:
```text
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"
```text

Resultado observado:

NAMES                IMAGE                     PORTS
wordpress_app        wordpress:php8.3-apache   0.0.0.0:8080->80/tcp
mariadb_pressbooks   mariadb:11                3306/tcp
postgres_db          postgres:17               0.0.0.0:5433->5432/tcp

El contenedor relevante para esta integración es:
```text
wordpress_app
```
y PostgreSQL:
```text
postgres_db
```

# 4. Verificación de FastAPI

Se verificó que FastAPI se ejecuta mediante Uvicorn en:
```text
127.0.0.1:8000
```
Comando:
```text
ss -ltnp | grep ':8000'
```
Cuando Uvicorn está activo debe aparecer un proceso escuchando en el puerto 8000.

# 5. Prueba A - API local

Objetivo

Comprobar que FastAPI responde directamente desde el sistema anfitrión.

Comando
```text
curl --max-time 10 -s \
  -o /tmp/api-users.json \
  -w "HTTP_STATUS=%{http_code}\n" \
  http://127.0.0.1:8000/api/users
```
Resultado
```text
HTTP_STATUS=200
```
Interpretación

La API está disponible y el endpoint:
```text
GET /api/users
```
responde correctamente.

# 6. Validación del JSON

Se utilizó:
```text
python -m json.tool /tmp/api-users.json
```
La respuesta contiene usuarios almacenados.

Ejemplo:
```text
{
    "login": "OscarClavijo-Dev",
    "name": null,
    "email": null,
    "avatar_url": "https://avatars.githubusercontent.com/...",
    "html_url": "https://github.com/OscarClavijo-Dev"
}
```
Resultado
```text
JSON válido
```
# 7. Prueba B - API desde WordPress

Objetivo

Comprobar que el contenedor WordPress puede acceder a FastAPI.

Comando
```text
docker exec wordpress_app curl \
  --max-time 10 \
  -s \
  -o /tmp/api-users.json \
  -w "HTTP_STATUS=%{http_code}\n" \
  http://host.docker.internal:8000/api/users
```
Resultado
```text
HTTP_STATUS=200
```
Interpretación

Esta prueba confirma la comunicación real:

```text
Docker / WordPress
        |
        v
host.docker.internal
        |
        v
FastAPI
```

Por lo tanto, la integración entre el contenedor WordPress y la API es funcional.

# 8. Inspección de respuesta desde WordPress

Se comprobó el contenido obtenido:
```text
docker exec wordpress_app sh -c \
'cat /tmp/api-users.json'
```
Se obtuvieron registros JSON de usuarios.

Esto demuestra que WordPress puede recuperar la información expuesta por FastAPI.

# 9. Prueba C - Sintaxis PHP

Objetivo

Verificar que el plugin no contiene errores sintácticos.

Comando local
```text
php -l wordpress-plugin/github-users/github-users.php
```
Resultado
```text
No syntax errors detected in wordpress-plugin/github-users/github-users.php
```
# 10. Prueba D - Sintaxis PHP dentro del contenedor

También se comprobó el archivo instalado dentro de WordPress:
```text
docker exec wordpress_app php -l \
  /var/www/html/wp-content/plugins/github-users/github-users.php
```
Resultado:
```text
No syntax errors detected
```
# 11. Prueba E - Archivos del plugin

Se verificó que WordPress tiene los archivos necesarios:
```text
docker exec wordpress_app sh -c \
'ls -lh \
/var/www/html/wp-content/plugins/github-users/github-users.php \
/var/www/html/wp-content/plugins/github-users/assets/css/github-users.css'
```
Resultado observado:
```text
github-users.php
github-users.css
```
Esto confirma que el plugin y su hoja de estilos fueron copiados correctamente al contenedor.

# 12. Prueba F - Respuesta de WordPress

Se verificó la página mediante:
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
WordPress responde correctamente.

# 13. Prueba G - Datos de la API presentes en WordPress

Se verificó que la respuesta HTML contiene un usuario recuperado desde la API.

Comando:
```text
grep -o "OscarClavijo-Dev" /tmp/wordpress.html | head
```

Resultado observado:
```text
OscarClavijo-Dev
OscarClavijo-Dev
OscarClavijo-Dev
Interpretación
```

Esta prueba demuestra que el contenido de la API no solamente está disponible de forma independiente, sino que fue incorporado a la página de WordPress.

# 14. Prueba H - Validación visual

Se accedió desde el navegador a la página de WordPress.

La vista presenta:
```text
Usuarios GitHub
```
y tarjetas con:
```text
Avatar.
Login.
Nombre.
Email.
Enlace de GitHub.
```

La información observada corresponde a los datos obtenidos mediante:

```text
GET /api/users
```

# 15. Prueba I - Campos nulos

La API contiene usuarios con campos opcionales null.

Por ejemplo:
```text
{
    "login": "OscarClavijo-Dev",
    "name": null,
    "email": null
}
```
La interfaz no falla.

En su lugar presenta:

Sin nombre
Sin email

Esto valida el manejo básico de campos opcionales.

# 16. Prueba J - Enlace a GitHub

Se validaron los botones:

Ver perfil en GitHub

Los enlaces existentes permiten acceder al perfil correspondiente.

Cuando una URL externa no está disponible, el enlace puede no conducir a un recurso válido; esto corresponde a la información recibida desde la fuente de datos y no impide la renderización de la vista.

# 17. Prueba K - Enlace a la API REST

La vista incluye:

Consultar API REST

El enlace apunta a:
```text
http://host.docker.internal:8000/api/users
```

Su finalidad es permitir consultar directamente la respuesta JSON del endpoint.

La funcionalidad fue corregida y validada durante las pruebas.

# 18. Prueba L - Comparación API / WordPress

Se verificó que un usuario presente en:
```text
GET /api/users
```
también aparece en WordPress.

Ejemplo:
```text
API:
OscarClavijo-Dev

WordPress:
OscarClavijo-Dev

Esto valida la transferencia de información entre la API y la aplicación principal.
```
# 19. Matriz de resultados

ID	Prueba	Resultado
A	FastAPI responde localmente	✅
B	WordPress accede a FastAPI	✅
C	Sintaxis PHP local	✅
D	Sintaxis PHP dentro de WordPress	✅
E	Archivos del plugin presentes	✅
F	WordPress responde HTTP 200	✅
G	Datos API presentes en HTML	✅
H	Vista visual funcionando	✅
I	Campos null controlados	✅
J	Enlaces a GitHub	✅
K	Enlace de consulta API	✅
L	Datos API y WordPress coinciden	✅

# 20. Resultado final

Las pruebas realizadas demuestran que:
```text
FastAPI
   |
   | HTTP
   v
WordPress
   |
   v
Plugin PHP
   |
   v
Vista HTML

funciona correctamente.

También se comprobó la comunicación entre:

Contenedor WordPress
        |
        v
host.docker.internal:8000
        |
        v
FastAPI

```
# 21. Evidencias recomendadas

Para la entrega se recomienda conservar capturas de:

- docker ps.
- FastAPI ejecutándose con Uvicorn.
- GET /api/users en terminal.
- Respuesta JSON.
- WordPress mostrando los usuarios.
- Código del plugin.
- Enlace "Consultar API REST".
- API REST abierta desde el navegador.
- Estructura del repositorio.
- Diagrama de flujo de integración.

Las capturas pueden almacenarse en:
```text
docs/evidencias/
```
# 22. Reproducción por parte del evaluador

Para reproducir la integración, el evaluador debe:

Paso 1

Clonar o descargar el repositorio.

Paso 2

Instalar las dependencias del proyecto.

Paso 3

Levantar PostgreSQL mediante Docker.

Paso 4

Ejecutar las migraciones necesarias.

Paso 5

Levantar FastAPI:
```text
source .venv/bin/activate

uvicorn app.main:app \
  --reload \
  --host 127.0.0.1 \
  --port 8000
```
Paso 6

Levantar WordPress:
```text
docker compose up -d
```
Paso 7

Instalar o copiar el plugin:
```text
wordpress-plugin/github-users/
```
a:
```text
wp-content/plugins/github-users/
```
Paso 8

Activar el plugin desde WordPress.

Paso 9

Crear una página con:
```text
[github_users]
```
Paso 10

Abrir:
```text
http://127.0.0.1:8080
```
y acceder a la página de usuarios.

# 23. Condición necesaria para la integración

FastAPI debe estar ejecutándose mientras se consulta la página de WordPress.

Si FastAPI está detenido, WordPress no podrá recuperar los usuarios y el plugin mostrará un mensaje de error.

Esto es esperado porque la página depende de la API propia.

# 24. Conclusión

Las pruebas confirman que la integración del Nivel 6 es funcional.

Se verificó:

- Comunicación API.
- Comunicación Docker → API.
- Integración PHP.
- Shortcode.
- Renderización HTML.
- Manejo de campos opcionales.
- Enlaces.
- Consulta de la API.
- Presentación de datos reales.

Por tanto, el Nivel 6 puede considerarse técnicamente validado.