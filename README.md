# Prueba Técnica – Soporte y Desarrollo

Solución desarrollada para el proceso de selección del cargo de **Soporte y Desarrollo**.

El proyecto demuestra capacidades de infraestructura, contenedores, consumo e integración de APIs, procesamiento de información, persistencia de datos, desarrollo de una API REST propia, integración entre componentes y documentación técnica.

La solución fue desarrollada progresivamente siguiendo los niveles establecidos en la prueba técnica.

---

# 1. Descripción general de la solución

La solución integra una aplicación web basada en WordPress, un plugin personalizado desarrollado en PHP, una API REST propia desarrollada con FastAPI y una base de datos PostgreSQL.

El sistema utiliza información obtenida desde la API de GitHub, procesa los datos y los almacena en PostgreSQL.

Posteriormente, la API propia permite consultar y gestionar la información almacenada.

Finalmente, el plugin personalizado de WordPress consume la API propia y presenta la información dentro de la aplicación principal.

La arquitectura actual combina servicios Docker con FastAPI ejecutándose localmente mediante un entorno virtual de Python.

El flujo principal es:

```text
                         USUARIO
                            │
                            ▼
                    WORDPRESS :8080
                            │
                            ▼
                  PLUGIN PERSONALIZADO PHP
                            │
                            │ HTTP
                            ▼
                    FASTAPI :8000
                            │
                       SQLAlchemy
                            │
                            ▼
                    POSTGRESQL :5433
                            ▲
                            │
                            │ Persistencia
                            │
                   Procesamiento de datos
                            ▲
                            │
                            │ HTTPS + Bearer Token
                            │
                       GITHUB API
```

---

# 2. Objetivo

Diseñar e implementar progresivamente una solución tecnológica que permita demostrar capacidades de:

* Infraestructura.
* Docker y contenedores.
* Administración de servicios.
* Consumo de APIs externas.
* Autenticación mediante tokens.
* Procesamiento de información.
* Persistencia de datos.
* Diseño y desarrollo de APIs REST.
* Integración entre aplicaciones.
* Desarrollo de plugins para WordPress.
* Documentación técnica.
* Control de versiones mediante Git.
* Reproducción de la solución en otro entorno.

---

# 3. Estado del proyecto

| Nivel   | Descripción                       | Estado                                                   |
| ------- | --------------------------------- | -------------------------------------------------------- |
| Nivel 1 | Preparación y Docker              | ✅ Finalizado                                             |
| Nivel 2 | Pressbooks / aplicación principal | ✅ Finalizado mediante alternativa documentada            |
| Nivel 3 | Consumo de API externa            | ✅ Finalizado                                             |
| Nivel 4 | Procesamiento y almacenamiento    | ✅ Finalizado                                             |
| Nivel 5 | Desarrollo de API propia          | ✅ Finalizado                                             |
| Nivel 6 | Integración entre componentes     | ✅ Finalizado                                             |
| Nivel 7 | Publicación de la solución        | ✅ Finalizado mediante estrategia alternativa documentada |
| Nivel 8 | Documentación y presentación      | ✅ Finalizado                                   |

---

# 4. Arquitectura utilizada

## 4.1 Arquitectura actual

```text
                              USUARIO
                                 │
                                 ▼
                         WORDPRESS :8080
                                 │
                                 ▼
                      PLUGIN PERSONALIZADO PHP
                                 │
                                 │ HTTP GET
                                 ▼
                         FASTAPI :8000
                                 │
                         ┌───────┴────────┐
                         │                │
                         ▼                ▼
                    SQLAlchemy       GitHub API
                         │                │
                         ▼                │
                    PostgreSQL 17 ◄───────┘
```

## 4.2 Componentes

### WordPress

Aplicación web principal utilizada para presentar la información al usuario.

Se ejecuta dentro del contenedor:

```text
wordpress_app
```

Puerto:

```text
8080 → 80
```

Acceso:

```text
http://127.0.0.1:8080
```

### Plugin personalizado

Se encuentra en:

```text
wordpress-plugin/github-users/
```

Archivos principales:

```text
wordpress-plugin/github-users/github-users.php
wordpress-plugin/github-users/assets/css/github-users.css
```

El plugin utiliza:

```text
[github_users]
```

para presentar la información obtenida desde la API propia.

### FastAPI

API REST desarrollada en Python.

Se ejecuta actualmente directamente en Fedora mediante el entorno virtual del proyecto.

Proceso utilizado:

```text
.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### PostgreSQL

Base de datos utilizada para la persistencia de la información.

Contenedor:

```text
postgres_db
```

Mapeo:

```text
5433 → 5432
```

### MariaDB

Existe un contenedor MariaDB utilizado en el entorno relacionado con Pressbooks:

```text
mariadb_pressbooks
```

Puerto interno:

```text
3306
```

Este servicio es independiente de PostgreSQL.

---

# 5. Tecnologías seleccionadas

## Backend

* Python 3.
* FastAPI.
* Uvicorn.
* SQLAlchemy.

## Base de datos

* PostgreSQL 17.

## Aplicación web

* WordPress.
* PHP.
* Plugin personalizado.

## API externa

* GitHub API.
* HTTP/HTTPS.
* Bearer Token.

## Infraestructura

* Docker.
* Docker Compose.
* Fedora Linux.

## Control de versiones

* Git.
* GitHub.

## Pruebas

* curl.
* Swagger UI / OpenAPI.
* Insomnia.
* `php -l`.

---

# 6. Estructura del repositorio

La estructura principal del proyecto es:

```text
.
├── app/
├── docs/
├── wordpress-plugin/
├── pressbooks/
├── scripts/
├── Insomnia/
├── README.md
└── ...
```

## `app/`

Contiene la aplicación FastAPI, modelos, lógica y componentes relacionados con el backend.

## `docs/`

Contiene documentación técnica, pruebas, integración, publicación y evidencias.

## `wordpress-plugin/`

Contiene el plugin personalizado de WordPress.

## `pressbooks/`

Contiene elementos relacionados con la investigación y configuración de Pressbooks.

## `scripts/`

Contiene scripts auxiliares del proyecto.

## `Insomnia/`

Contiene recursos utilizados para las pruebas y consultas HTTP.

---

# 7. Requisitos previos

Para ejecutar la solución localmente se requiere:

* Linux/Fedora u otra distribución compatible.
* Git.
* Docker.
* Docker Compose.
* Python 3.
* `venv`.
* pip.
* Navegador web.
* Conexión a Internet para consumir la API externa.
* Token de GitHub configurado mediante variables de entorno.

Comprobar Docker:

```bash
docker --version
docker compose version
```

Comprobar Python:

```bash
python3 --version
```

Comprobar Git:

```bash
git --version
```

---

# 8. Instalación

## 8.1 Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Prueba_Tecnica_Oscar_Clavijo
```

## 8.2 Crear entorno virtual

```bash
python3 -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

## 8.3 Instalar dependencias

Si el repositorio contiene `requirements.txt`:

```bash
pip install -r requirements.txt
```

Si las dependencias se gestionan mediante otro archivo de configuración Python, utilizar el mecanismo definido por el proyecto.

---

# 9. Configuración de variables de entorno

Las credenciales y configuraciones sensibles deben mantenerse fuera del código fuente.

El proyecto utiliza variables de entorno para información como:

* Token de GitHub.
* Usuario de PostgreSQL.
* Contraseña de PostgreSQL.
* Nombre de la base de datos.
* Host de PostgreSQL.
* Puerto de PostgreSQL.
* Configuración de la aplicación.

Se debe utilizar:

```text
.env.example
```

como plantilla para preparar el entorno local.

Las credenciales reales deben almacenarse en:

```text
.env
```

y este archivo no debe incluirse en Git.

Nunca se debe almacenar directamente un token de GitHub dentro del código fuente.

---

# 10. Inicio de PostgreSQL y WordPress

Los servicios Docker utilizados por la solución pueden comprobarse mediante:

```bash
docker ps
```

La configuración actual utiliza los siguientes contenedores principales:

```text
wordpress_app
postgres_db
mariadb_pressbooks
```

Para levantar los servicios definidos mediante Compose:

```bash
docker compose up -d
```

Verificar:

```bash
docker ps
```

Para consultar logs:

```bash
docker compose logs
```

o:

```bash
docker compose logs <servicio>
```

---

# 11. Inicio de FastAPI

FastAPI se ejecuta actualmente desde el entorno virtual Python del proyecto.

Activar el entorno:

```bash
source .venv/bin/activate
```

Iniciar Uvicorn:

```bash
.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
```

La API queda disponible en:

```text
http://127.0.0.1:8000
```

El proceso utilizado durante la validación es:

```text
/home/oscarclavijo/Documentos/Prueba_Tecnica_Oscar_Clavijo/.venv/bin/python3
/home/oscarclavijo/Documentos/Prueba_Tecnica_Oscar_Clavijo/.venv/bin/uvicorn
app.main:app
--host 127.0.0.1
--port 8000
```

Para verificar que el puerto está escuchando:

```bash
ss -ltnp | grep ':8000'
```

---

# 12. Accesos y puertos

| Componente |   Host | Contenedor | Acceso                  |
| ---------- | -----: | ---------: | ----------------------- |
| WordPress  | `8080` |       `80` | `http://127.0.0.1:8080` |
| PostgreSQL | `5433` |     `5432` | `127.0.0.1:5433`        |
| MariaDB    |      — |     `3306` | Red interna Docker      |
| FastAPI    | `8000` |          — | `http://127.0.0.1:8000` |

## URLs principales

WordPress:

```text
http://127.0.0.1:8080
```

FastAPI:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

OpenAPI:

```text
http://127.0.0.1:8000/openapi.json
```

API de usuarios:

```text
http://127.0.0.1:8000/api/users
```

---

# 13. Configuración de la API externa

La solución utiliza la API de GitHub como fuente externa.

La comunicación se realiza mediante HTTPS y autenticación mediante Bearer Token.

Flujo:

```text
Aplicación
    │
    │ HTTPS
    │ Authorization: Bearer <TOKEN>
    ▼
GitHub API
    │
    ▼
Información externa
```

El token se configura mediante variables de entorno.

El flujo permite:

1. Consultar información de GitHub.
2. Procesar los datos.
3. Persistirlos en PostgreSQL.
4. Exponerlos mediante la API propia.
5. Consultarlos desde WordPress.

---

# 14. Modelo de datos

La persistencia principal se realiza mediante PostgreSQL 17.

La entidad principal es:

```text
github_users
```

Flujo:

```text
GitHub API
    │
    ▼
Procesamiento
    │
    ▼
SQLAlchemy
    │
    ▼
PostgreSQL 17
    │
    ▼
github_users
```

El almacenamiento local permite consultar la información sin depender exclusivamente de una solicitud directa a GitHub para cada consulta de la aplicación.

---

# 15. Documentación de la API propia

La API fue desarrollada con FastAPI y proporciona documentación OpenAPI automática.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

OpenAPI:

```text
http://127.0.0.1:8000/openapi.json
```

## Endpoints

### Obtener usuarios

```http
GET /api/users
```

Consulta los usuarios almacenados.

### Obtener usuario

```http
GET /api/users/{id}
```

Consulta un usuario específico.

### Crear usuario

```http
POST /api/users
```

Crea un nuevo registro.

### Actualizar usuario

```http
PUT /api/users/{id}
```

Actualiza un registro existente.

### Eliminar usuario

```http
DELETE /api/users/{id}
```

Elimina un registro.

La API también incorpora:

* Filtros.
* Paginación.

---

# 16. Integración WordPress → FastAPI

El plugin personalizado se encuentra en:

```text
wordpress-plugin/github-users/
```

Archivos principales:

```text
wordpress-plugin/github-users/github-users.php
wordpress-plugin/github-users/assets/css/github-users.css
```

El shortcode utilizado es:

```text
[github_users]
```

## Flujo

```text
Usuario
   │
   ▼
WordPress
   │
   ▼
[github_users]
   │
   ▼
Plugin PHP
   │
   │ HTTP GET
   ▼
FastAPI
   │
   ▼
PostgreSQL
   │
   ▼
JSON
   │
   ▼
Plugin PHP
   │
   ▼
WordPress
```

## Comunicación Docker → host

WordPress se ejecuta dentro de Docker, mientras FastAPI se ejecuta directamente en Fedora.

Por este motivo, desde el contenedor WordPress la API se consulta mediante:

```text
http://host.docker.internal:8000/api/users
```

No se utiliza:

```text
http://127.0.0.1:8000/api/users
```

desde WordPress, porque dentro de un contenedor `127.0.0.1` representa el propio contenedor y no el host Fedora.

Esta configuración fue validada durante el Nivel 6.

---

# 17. Pruebas realizadas

## 17.1 API FastAPI

Validación mediante cURL:

```bash
curl --max-time 10 -s \
  -o /tmp/api-users.json \
  -w "HTTP_STATUS=%{http_code}\n" \
  http://127.0.0.1:8000/api/users
```

Resultado validado:

```text
HTTP_STATUS=200
```

## 17.2 Acceso desde WordPress

Desde el contexto de Docker se verificó el acceso mediante:

```text
http://host.docker.internal:8000/api/users
```

Resultado validado:

```text
HTTP_STATUS=200
```

## 17.3 Validación PHP

```bash
docker exec wordpress_app php -l \
/var/www/html/wp-content/plugins/github-users/github-users.php
```

Resultado validado:

```text
No syntax errors detected
```

## 17.4 WordPress

Se verificó:

* Respuesta HTTP 200.
* Carga de la página.
* Plugin activo.
* Shortcode funcionando.
* Información obtenida desde FastAPI.
* Presentación de usuarios en la interfaz.

## 17.5 Integración completa

El flujo:

```text
WordPress
   ↓
Plugin PHP
   ↓ HTTP
FastAPI
   ↓
PostgreSQL
```

fue validado correctamente.

---

# 18. Evidencias

Las evidencias se encuentran en:

```text
docs/evidencias/
```

Se incluyen evidencias relacionadas con:

* Documentación Swagger.
* Endpoints de FastAPI.
* Consulta individual.
* Aplicación WordPress.
* Integración WordPress → FastAPI.
* Contenedores Docker.
* Ejecución de Uvicorn.
* Pruebas cURL.
* Validación del plugin PHP.
* Estado del repositorio.

Las evidencias visuales complementan las pruebas técnicas documentadas en:

```text
docs/24-Integracion-WordPress-FastAPI.md
docs/25-Flujo-Integracion.md
docs/26-Pruebas-Integracion.md
docs/27-Publicacion-Solucion.md
```

---

# 19. Proceso de despliegue

## 19.1 Despliegue local

La estrategia utilizada para la entrega es un entorno local reproducible.

```text
Git
 │
 ▼
Repositorio
 │
 ├───────────────┐
 ▼               ▼
Docker          Fedora
 │               │
 ├─ WordPress    └─ FastAPI/Uvicorn
 │
 ├─ PostgreSQL
 │
 └─ MariaDB
```

Los componentes se comunican de la siguiente manera:

```text
WordPress
    │
    │ host.docker.internal:8000
    ▼
FastAPI
    │
    ▼
PostgreSQL
```

FastAPI, a su vez, puede interactuar con la API externa de GitHub.

## 19.2 Publicación en Internet

El Nivel 7 solicitaba idealmente disponer de la solución desde Internet.

Se evaluaron alternativas como:

* Servidor propio.
* VPS.
* Render.
* Railway.
* Fly.io.
* AWS.
* Azure.
* Google Cloud.
* Cloudflare Tunnel.
* Ngrok.

No se mantiene una publicación permanente en Internet para esta entrega.

La prueba técnica contempla expresamente, cuando no sea posible mantener la solución publicada, la entrega de:

* Capturas.
* Evidencias de ejecución.
* Instrucciones completas para ejecutar localmente.
* Explicación de la estrategia de despliegue.

Por este motivo, el Nivel 7 se entrega mediante una estrategia local reproducible y evidencias verificables.

La justificación detallada se encuentra en:

```text
docs/27-Publicacion-Solucion.md
```

---

# 20. Limitaciones conocidas

## Publicación permanente

La solución no mantiene una instancia pública permanente en Internet.

La infraestructura utilizada para la validación es local.

## Dependencia del entorno local

Para ejecutar la solución se requiere que los servicios correspondientes estén activos.

## Pressbooks

Pressbooks fue investigado e intentado inicialmente.

Debido a las dificultades encontradas para disponer de un entorno funcional dentro del alcance de la prueba, se utilizó WordPress como alternativa documentada.

## API externa

La funcionalidad que depende de información de GitHub requiere:

* Conectividad a Internet.
* Disponibilidad de la API.
* Token correctamente configurado.

## Puertos

Los puertos utilizados corresponden al entorno local actual y pueden modificarse mediante la configuración de Docker.

---

# 21. Problemas encontrados

## Pressbooks

Se presentaron dificultades para disponer de un entorno Pressbooks funcional dentro del alcance de la prueba.

### Solución

Se utilizó WordPress como aplicación principal alternativa, documentando la decisión.

## Comunicación entre Docker y Fedora

WordPress se ejecuta dentro de Docker y FastAPI directamente sobre Fedora.

Fue necesario utilizar:

```text
host.docker.internal
```

para permitir que WordPress accediera al servicio FastAPI del host.

## Integración WordPress → FastAPI

Se validaron:

* URL.
* Accesibilidad.
* Respuesta HTTP.
* Sintaxis PHP.
* Archivos dentro del contenedor.
* Presentación visual.

## Publicación

Se evaluaron mecanismos de publicación permanente y temporal.

La estrategia final priorizó la reproducción local y las evidencias permitidas por la prueba frente a una publicación temporal dependiente de infraestructura local.

---

# 22. Decisiones técnicas

## FastAPI

Seleccionado por:

* Desarrollo rápido.
* Tipado.
* Documentación OpenAPI automática.
* Swagger UI.
* Adecuación para APIs REST.

## PostgreSQL

Seleccionado por:

* Modelo relacional.
* Integridad de datos.
* Robustez.
* Compatibilidad con SQLAlchemy.

## Docker

Utilizado para:

* Aislamiento.
* Reproducibilidad.
* Separación de servicios.
* Configuración consistente.

## WordPress

Utilizado como alternativa a Pressbooks debido a las dificultades de disponer de un entorno funcional de Pressbooks dentro del alcance de la prueba.

## Plugin personalizado

Permite demostrar una integración real entre la aplicación web y la API propia.

## Git

Utilizado para:

* Control de versiones.
* Trazabilidad.
* Recuperación de cambios.
* Entrega reproducible.

---

# 23. Aspectos pendientes

Los siguientes aspectos quedan fuera del alcance funcional actual, pero pueden desarrollarse posteriormente:

* Publicación permanente en infraestructura cloud.
* Dominio y HTTPS productivo.
* CI/CD.
* Gestión avanzada de secretos.
* Monitoreo.
* Logging centralizado.
* Backups automatizados.
* Hardening de infraestructura.
* Pruebas automatizadas adicionales.
* Cobertura de pruebas.
* Migración completa a Pressbooks si se requiere específicamente dicha plataforma.

---

# 24. Mejoras futuras

## Infraestructura

* VPS o cloud.
* Reverse proxy.
* HTTPS.
* Gestión de secretos.
* Backups automatizados.
* Monitoreo.

## API

* Autenticación y autorización.
* Rate limiting.
* Versionado.
* Manejo estandarizado de errores.
* Pruebas automatizadas.
* Observabilidad.

## Base de datos

* Migraciones mediante Alembic.
* Índices adicionales.
* Optimización de consultas.
* Estrategia de backup y recuperación.

## WordPress

* Mejoras de interfaz.
* Configuración administrativa del plugin.
* Manejo avanzado de errores.
* Caché.
* Mejor integración visual.

## DevOps

* GitHub Actions.
* CI/CD.
* Automatización de pruebas.
* Construcción automática de imágenes.
* Despliegue automatizado.

---

# 25. Documentación complementaria

La documentación técnica se encuentra en:

```text
docs/
```

Documentación de integración:

```text
docs/24-Integracion-WordPress-FastAPI.md
docs/25-Flujo-Integracion.md
docs/26-Pruebas-Integracion.md
```

Documentación de publicación:

```text
docs/27-Publicacion-Solucion.md
```

Evidencias:

```text
docs/evidencias/
```

---

# 26. Reproducción de la solución

## Paso 1 – Clonar

```bash
git clone <URL_DEL_REPOSITORIO>
cd Prueba_Tecnica_Oscar_Clavijo
```

## Paso 2 – Configurar Python

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Paso 3 – Configurar variables

Crear el archivo local:

```text
.env
```

tomando como referencia:

```text
.env.example
```

Configurar las credenciales necesarias.

## Paso 4 – Levantar infraestructura Docker

```bash
docker compose up -d
```

Verificar:

```bash
docker ps
```

## Paso 5 – Iniciar FastAPI

En otra terminal:

```bash
cd Prueba_Tecnica_Oscar_Clavijo
source .venv/bin/activate
.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## Paso 6 – Comprobar FastAPI

```bash
curl http://127.0.0.1:8000/api/users
```

## Paso 7 – Abrir Swagger

```text
http://127.0.0.1:8000/docs
```

## Paso 8 – Abrir WordPress

```text
http://127.0.0.1:8080
```

## Paso 9 – Comprobar integración

Acceder a la página de WordPress que utiliza:

```text
[github_users]
```

El plugin debe consultar:

```text
http://host.docker.internal:8000/api/users
```

y mostrar los usuarios obtenidos desde la API propia.

---

# 27. Seguridad y credenciales

No se deben almacenar credenciales reales en Git.

Se deben proteger especialmente:

* Token de GitHub.
* Contraseña de PostgreSQL.
* Credenciales administrativas.
* Secretos de aplicación.

El archivo local:

```text
.env
```

no debe incluirse en el repositorio.

Debe mantenerse una plantilla:

```text
.env.example
```

sin credenciales reales.

---

# 28. Control de versiones

El proyecto utiliza Git.

Antes de realizar cambios:

```bash
git status
```

Validación de espacios y errores:

```bash
git diff --check
```

Antes de realizar un commit:

```bash
git add .
git diff --cached --stat
git diff --cached --check
```

El repositorio mantiene la trazabilidad de la implementación de los diferentes niveles de la prueba.

---

# 29. Estado final de la solución

La solución implementa y demuestra:

* Infraestructura Docker.
* WordPress como aplicación principal.
* Plugin personalizado PHP.
* Consumo de API externa de GitHub.
* Autenticación mediante Bearer Token.
* Procesamiento de información.
* Persistencia PostgreSQL 17.
* API REST propia con FastAPI.
* Operaciones CRUD.
* Filtros.
* Paginación.
* Documentación OpenAPI/Swagger.
* Integración WordPress → FastAPI.
* Evidencias técnicas.
* Documentación de despliegue.
* Reproducción local.
* Control de versiones mediante Git.

El proyecto queda preparado para evaluación técnica mediante ejecución local y las evidencias incluidas en el repositorio.
