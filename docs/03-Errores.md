# Registro de Errores

## Error 001

### Fecha

24/07/2026

### Etapa

Sprint 1 - Instalación de Docker

### Comando ejecutado

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Error obtenido

```
No coincide para argumento: docker-ce
No coincide para argumento: docker-ce-cli
No coincide para argumento: containerd.io
No coincide para argumento: docker-buildx-plugin
No coincide para argumento: docker-compose-plugin
```

### Análisis preliminar

El sistema no encontró los paquetes solicitados. Antes de continuar con la instalación es necesario verificar que el repositorio oficial de Docker haya sido agregado y habilitado correctamente.

### Estado

### Causa raíz

Se verificó que el repositorio oficial de Docker no estaba registrado en el sistema. Al no existir el archivo `docker-ce.repo`, DNF no podía localizar los paquetes `docker-ce`, `docker-ce-cli`, `containerd.io` y los demás componentes.

### Solución aplicada

Se volvió al paso de configuración del repositorio oficial de Docker para agregarlo correctamente antes de intentar nuevamente la instalación.

### Lección aprendida

Antes de instalar paquetes desde un repositorio externo, es recomendable verificar que dicho repositorio quedó registrado correctamente mediante `dnf repolist` y comprobando la existencia del archivo correspondiente en `/etc/yum.repos.d/`.

## Error 002

### Fecha

24/07/2026

### Etapa

Sprint 1 - Configuración de Docker Compose

### Comando ejecutado

```bash
docker compose up -d
```

### Error obtenido

```text
Error response from daemon:
ports are not available:
listen tcp 0.0.0.0:5432:
bind: address already in use
```

### Análisis preliminar

Docker no pudo iniciar el contenedor porque el puerto 5432 del sistema anfitrión ya estaba siendo utilizado por otro proceso.

### Posibles causas

- PostgreSQL instalado en el sistema operativo.
- Otro contenedor Docker.
- Un servicio ejecutándose mediante Podman.


# ERROR-003 — ModuleNotFoundError: No module named 'app'

## 1. Información general

| Campo | Detalle |
|---|---|
| Identificador | ERROR-002 |
| Nivel | Nivel 3 — Consumo de API externa |
| Componente | FastAPI / Servicio GitHub |
| Tecnología | Python |
| Entorno | Fedora 44 |
| Entorno virtual | `.venv` |
| Archivo ejecutado | `scripts/test_github.py` |
| Error | `ModuleNotFoundError: No module named 'app'` |
| Estado | Resuelto |

---

# 2. Contexto

Durante la implementación del Nivel 3 se creó un servicio Python encargado de consumir la API de GitHub.

La estructura del proyecto separa la aplicación principal de los scripts de prueba:

```text
Prueba_Tecnica_Oscar_Clavijo/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── services/
│       ├── __init__.py
│       └── github_service.py
│
├── scripts/
│   └── test_github.py
│
├── .venv/
├── requirements.txt
├── docker-compose.yml
└── README.md