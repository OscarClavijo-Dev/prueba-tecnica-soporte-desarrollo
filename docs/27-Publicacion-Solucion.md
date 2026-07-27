# Nivel 7 – Publicación de la solución

## 1. Objetivo

El objetivo de este nivel es establecer una estrategia para que la solución desarrollada pueda ser evaluada, ya sea mediante una publicación accesible desde Internet o, cuando esto no sea posible de forma permanente, mediante evidencias reproducibles de ejecución local.

La solución desarrollada está compuesta por:

* Una aplicación principal basada en WordPress/Pressbooks.
* Un plugin personalizado desarrollado en PHP.
* Una API REST desarrollada con FastAPI.
* PostgreSQL como sistema de persistencia.
* SQLAlchemy como capa de acceso a datos.
* Docker para la ejecución de los componentes.
* Integración con información obtenida desde una API externa de GitHub.

La integración entre los componentes fue implementada y validada previamente en el Nivel 6.

---

## 2. Requisito de la prueba

El Nivel 7 solicita publicar la solución para que pueda ser evaluada desde Internet.

Idealmente, la prueba establece que deberían estar disponibles:

* La instancia de Pressbooks o aplicación principal.
* La API desarrollada.
* La documentación de la API.

La prueba contempla como alternativas:

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
* Otra alternativa seleccionada por el candidato.

La prueba también establece que, cuando no sea posible mantener la solución publicada, se pueden entregar:

* Video demostrativo.
* Capturas de pantalla.
* Evidencias de ejecución.
* Instrucciones completas para ejecutarla localmente.
* Explicación de la estrategia de despliegue.

Finalmente, la prueba indica que la publicación en Internet tiene una valoración adicional, pero no constituye un requisito excluyente para presentar los avances.

---

## 3. Estado de publicación

Para esta entrega se decidió no mantener una instancia pública permanente de la solución.

La aplicación se encuentra completamente implementada y funcional en el entorno local de desarrollo, donde se validaron los componentes individuales y la integración entre WordPress, el plugin personalizado, FastAPI y PostgreSQL.

La entrega del Nivel 7 se respalda mediante:

* Capturas de pantalla.
* Evidencias de ejecución.
* Evidencias de funcionamiento de la API.
* Evidencia de la documentación OpenAPI/Swagger.
* Evidencia de la aplicación principal.
* Evidencia de la integración WordPress → FastAPI.
* Instrucciones de ejecución local.
* Estrategia de despliegue documentada.
* Documentación técnica del proyecto.

La decisión de no mantener una publicación permanente no implica que la solución no pueda ser desplegada. Se trata de una decisión relacionada con las condiciones de disponibilidad y reproducibilidad de la infraestructura utilizada para la prueba.

---

## 4. Aplicación principal

La aplicación principal utilizada en la solución es WordPress/Pressbooks.

La aplicación incorpora un plugin personalizado ubicado en:

```text
wordpress-plugin/github-users/
```

El plugin proporciona el shortcode:

```text
[github_users]
```

Este shortcode permite presentar en una página de WordPress la información obtenida desde la API propia.

El flujo principal es:

```text
Usuario
   ↓
WordPress / Pressbooks
   ↓
Plugin personalizado PHP
   ↓ HTTP
API FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

La integración fue implementada y validada durante el Nivel 6.

---

## 5. API desarrollada

La solución dispone de una API REST desarrollada con FastAPI.

Los principales endpoints implementados son:

```text
GET    /api/users
GET    /api/users/{id}
POST   /api/users
PUT    /api/users/{id}
DELETE /api/users/{id}
```

La API incorpora además funcionalidades de consulta mediante filtros y paginación.

La API se ejecuta localmente mediante un servidor ASGI utilizando Uvicorn.

La estructura permite separar las responsabilidades entre:

* Rutas HTTP.
* Lógica de aplicación.
* Modelos.
* Acceso a datos.
* Persistencia PostgreSQL.

La API fue validada previamente mediante solicitudes HTTP y pruebas de integración con WordPress.

---

## 6. Documentación de la API

FastAPI genera automáticamente la documentación interactiva de la API mediante OpenAPI.

La documentación puede consultarse localmente en:

```text
http://127.0.0.1:8000/docs
```

También se dispone del esquema OpenAPI en:

```text
http://127.0.0.1:8000/openapi.json
```

La interfaz Swagger permite consultar los endpoints disponibles y realizar pruebas directamente sobre la API durante la ejecución local.

La documentación constituye la referencia técnica para evaluar las operaciones disponibles en la API.

---

## 7. Estrategia de despliegue

Se evaluó la posibilidad de publicar la solución mediante una infraestructura externa o mediante un túnel seguro hacia el entorno local.

La estrategia de despliegue considerada se basa en mantener separadas las responsabilidades de los componentes:

```text
                Internet
                   │
                   ▼
        Aplicación principal
           WordPress/Pressbooks
                   │
                   ▼
            Plugin PHP
                   │
                HTTP
                   │
                   ▼
              FastAPI
                   │
                   ▼
             SQLAlchemy
                   │
                   ▼
             PostgreSQL
```

En un escenario de producción, WordPress y FastAPI podrían ejecutarse en infraestructura cloud o en un servidor/VPS con los servicios expuestos mediante HTTPS.

Para esta prueba, la prioridad fue mantener una solución reproducible, funcional y verificable sin introducir una dependencia obligatoria de infraestructura externa de pago o de disponibilidad permanente.

---

## 8. Alternativas evaluadas

### Servidor propio

Permitiría alojar directamente WordPress, FastAPI y PostgreSQL y controlar completamente la infraestructura.

Sin embargo, requiere disponer de un servidor permanentemente disponible, conectividad adecuada, configuración de red, seguridad, mantenimiento y disponibilidad continua.

No se seleccionó para esta entrega debido a la necesidad de garantizar disponibilidad permanente durante el periodo de evaluación.

### VPS

Un VPS permitiría disponer de una máquina virtual permanentemente accesible desde Internet.

Es una alternativa técnicamente adecuada para este tipo de arquitectura, pero normalmente implica contratar infraestructura o disponer de un crédito/promoción vigente.

No se seleccionó para esta entrega debido a la necesidad de mantener el proyecto sin una dependencia económica o de disponibilidad externa.

### Render

Render fue considerada como alternativa de despliegue administrado.

Puede simplificar el despliegue de aplicaciones web, pero las condiciones de los servicios gratuitos pueden incluir limitaciones de recursos, suspensión por inactividad, restricciones de persistencia o cambios en las condiciones del servicio.

Para esta prueba se priorizó una estrategia que no dependiera de esas restricciones para garantizar la reproducibilidad del proyecto.

### Railway

Railway permite desplegar aplicaciones y servicios mediante una plataforma administrada.

Sin embargo, sus condiciones de uso y disponibilidad gratuita pueden estar sujetas a límites, créditos o cambios en las políticas del servicio.

Por esta razón no se seleccionó como infraestructura definitiva para esta entrega.

### Fly.io

Fly.io permite desplegar aplicaciones próximas a los usuarios mediante infraestructura distribuida.

La alternativa fue considerada, pero introduciría una infraestructura externa adicional que no es necesaria para demostrar el funcionamiento de la solución y que podría estar sujeta a condiciones de uso y disponibilidad.

### AWS

AWS permite desplegar todos los componentes necesarios utilizando servicios como EC2, RDS u otros servicios administrados.

Es una alternativa adecuada para una arquitectura productiva, pero implica mayor complejidad operativa y puede requerir configuración de facturación, créditos o servicios con costos asociados.

No se consideró proporcional a los objetivos de esta prueba técnica.

### Azure

Azure ofrece servicios adecuados para alojar APIs, bases de datos y aplicaciones web.

Al igual que AWS, requiere gestionar infraestructura y servicios cloud y puede depender de créditos o condiciones específicas para disponer de recursos gratuitos.

No se seleccionó para esta entrega debido a que introduce una complejidad superior a la necesaria.

### Google Cloud

Google Cloud también permite implementar una arquitectura equivalente mediante máquinas virtuales y servicios administrados.

Aunque puede disponer de créditos o niveles gratuitos bajo determinadas condiciones, la configuración necesaria para una solución completa introduce infraestructura adicional que no resulta necesaria para demostrar el funcionamiento de la solución desarrollada.

### Cloudflare Tunnel

Cloudflare Tunnel fue considerada como alternativa para exponer temporalmente servicios locales a Internet sin abrir directamente puertos de entrada en el router.

Su principal limitación para esta entrega es que el servicio publicado depende de que la infraestructura local permanezca encendida y disponible.

Por lo tanto, no resuelve el requisito de disponer de una instancia permanentemente accesible cuando el equipo local está apagado.

No se seleccionó como mecanismo de publicación permanente.

### Ngrok

Ngrok permite crear túneles hacia servicios que se ejecutan localmente.

Al igual que Cloudflare Tunnel, la publicación depende de que el equipo local y los servicios permanezcan activos.

Por este motivo es útil para demostraciones o pruebas temporales, pero no se considera una solución permanente para esta entrega.

---

## 9. Estrategia seleccionada para la entrega

La estrategia seleccionada consiste en entregar la solución mediante un **entorno local completamente reproducible**, acompañado de evidencias técnicas suficientes para demostrar su funcionamiento.

Esta decisión se basa en cuatro criterios:

1. La solución ya se encuentra implementada y validada.
2. Los componentes pueden ejecutarse localmente mediante las tecnologías utilizadas durante el desarrollo.
3. Una publicación temporal mediante túnel requiere mantener el equipo local encendido durante el periodo de evaluación.
4. La propia prueba contempla expresamente la entrega mediante capturas, evidencias de ejecución, instrucciones locales y explicación de la estrategia de despliegue cuando no sea posible mantener la solución publicada.

Por lo tanto, la estrategia de entrega es:

```text
Repositorio Git
      ↓
Clonación
      ↓
Configuración local
      ↓
Docker
      ↓
PostgreSQL
      ↓
FastAPI + Uvicorn
      ↓
WordPress / Pressbooks
      ↓
Plugin personalizado
      ↓
Integración funcional
```

La publicación en Internet queda identificada como una posibilidad de despliegue adicional para una infraestructura disponible permanentemente.

---

## 10. Ejecución local

La solución puede ejecutarse localmente siguiendo las instrucciones descritas en el archivo `README.md`.

De manera general, el proceso comprende:

1. Clonar el repositorio.
2. Preparar las variables de entorno.
3. Levantar los servicios Docker requeridos.
4. Verificar PostgreSQL.
5. Ejecutar FastAPI mediante Uvicorn.
6. Verificar la documentación de FastAPI.
7. Acceder a WordPress/Pressbooks.
8. Activar el plugin personalizado.
9. Crear o acceder a la página que contiene el shortcode:

```text
[github_users]
```

10. Verificar la comunicación entre WordPress y FastAPI.
11. Comprobar la información obtenida desde PostgreSQL.

Las instrucciones detalladas de reproducción se encuentran en el `README.md` principal del repositorio.

---

## 11. Evidencias

Las evidencias del Nivel 7 se almacenan en:

```text
docs/evidencias/
```

Las principales evidencias incluyen:

| Evidencia                                        | Descripción                                           |
| ------------------------------------------------ | ----------------------------------------------------- |
| `evidencia-01-documentacion-api-swagger.png`     | Documentación interactiva de FastAPI mediante Swagger |
| `evidencia-02-api-users-get.png`                 | Respuesta del endpoint `/api/users`                   |
| `evidencia-03-api-user-id.png`                   | Consulta de un usuario mediante `/api/users/{id}`     |
| `evidencia-04-wordpress-aplicacion.png`          | Aplicación principal WordPress funcionando            |
| `evidencia-05-integracion-wordpress-fastapi.png` | Integración entre WordPress y FastAPI                 |
| `evidencia-06-contenedores-docker.png`           | Servicios ejecutándose mediante Docker                |
| `evidencia-07-fastapi-uvicorn.png`               | API ejecutándose mediante Uvicorn                     |
| `evidencia-08-curl-api.png`                      | Validación de la API mediante HTTP/cURL               |
| `evidencia-09-validacion-plugin-php.png`         | Validación sintáctica del plugin PHP                  |
| `evidencia-10-repositorio-limpio.png`            | Estado limpio del repositorio Git                     |

Estas evidencias complementan las pruebas realizadas durante los niveles anteriores.

---

## 12. Capturas

Las capturas permiten verificar visualmente los principales componentes de la solución.

### Documentación de la API

Archivo:

```text
docs/evidencias/evidencia-01-documentacion-api-swagger.png
```

Demuestra la disponibilidad de Swagger UI y los endpoints de la API.

### API

Archivo:

```text
docs/evidencias/evidencia-02-api-users-get.png
```

Demuestra la respuesta del endpoint principal de consulta.

### Consulta individual

Archivo:

```text
docs/evidencias/evidencia-03-api-user-id.png
```

Demuestra la consulta de un recurso individual.

### Aplicación principal

Archivo:

```text
docs/evidencias/evidencia-04-wordpress-aplicacion.png
```

Demuestra la interfaz de la aplicación principal.

### Integración

Archivo:

```text
docs/evidencias/evidencia-05-integracion-wordpress-fastapi.png
```

Demuestra el resultado de la integración entre WordPress y la API propia.

---

## 13. Reproducción de la solución

La solución está diseñada para ser reproducible mediante el repositorio Git.

El evaluador debe poder:

```text
Clonar repositorio
       ↓
Preparar entorno
       ↓
Levantar PostgreSQL
       ↓
Ejecutar FastAPI
       ↓
Levantar WordPress
       ↓
Activar plugin
       ↓
Acceder a la aplicación
       ↓
Consultar API
       ↓
Comprobar integración
```

La documentación principal de reproducción se encuentra en:

```text
README.md
```

La documentación técnica adicional se encuentra en:

```text
docs/
```

Incluyendo la documentación de integración desarrollada durante el Nivel 6.

---

## 14. Limitaciones

La principal limitación de la estrategia seleccionada es que el entorno de ejecución local no proporciona disponibilidad permanente desde Internet.

Las alternativas basadas en túneles, como Cloudflare Tunnel o Ngrok, permiten publicar servicios locales temporalmente, pero requieren que el equipo donde se ejecutan los servicios permanezca encendido y conectado a Internet.

Por otro lado, las plataformas cloud requieren evaluar cuidadosamente sus condiciones de disponibilidad, límites de recursos, persistencia, créditos o posibles costos para mantener una arquitectura completa compuesta por WordPress, FastAPI y PostgreSQL.

Por esta razón, para esta entrega se priorizó la **reproducibilidad local y la evidencia verificable del funcionamiento** frente a una publicación temporal que no pudiera garantizar disponibilidad permanente.

Esta decisión es coherente con el propio enunciado del Nivel 7, que contempla como alternativa las capturas, evidencias de ejecución, instrucciones completas de ejecución local y explicación de la estrategia de despliegue cuando no sea posible mantener la solución publicada.

La publicación permanente mediante infraestructura cloud queda como una posible etapa posterior de despliegue.

---

