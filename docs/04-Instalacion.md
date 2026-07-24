# Instalación del Entorno

## Información del sistema

        Sistema Operativo: FEdora Linux 44

        Kernel: 7.1.4-204.fc44.x86_64

        Arquitectura: x86_64


## Objetivo

Preparar un entorno de desarrollo reproducible basado en Docker para ejecutar todos los componentes de la prueba técnica de forma aislada y consistente.

## Requisitos Previos

    - Fedora 44 actualizado.
    - Conexión a Internet.
    - Git instalado.
    - Visual Studio Code.
    - Permisos de administrador (sudo).

    Componentes instalados:

    - Docker Engine
    - Docker CLI
    - Docker Compose Plugin
    - Containerd

    Durante la instalación se verificó la correcta configuración del repositorio oficial antes de instalar los paquetes.

## Instalación de Docker

    Se utilizó el repositorio oficial de Docker para Fedora.

## Docker Desktop

    Se instaló Docker Desktop sobre Fedora 44 como herramienta gráfica para administrar:

    - Contenedores
    - Imágenes
    - Redes
    - Volúmenes
    - Logs

    La instalación se realizó mediante el paquete RPM oficial distribuido por Docker.
    Se instaló Docker Desktop sobre Fedora 44 como herramienta gráfica para visualizar y administrar contenedores durante el desarrollo.

    La instalación se realizó mediante el paquete RPM oficial proporcionado por Docker.

## Configuración del Usuario

    Se configuró el servicio Docker para ejecutarse correctamente en Fedora.

## Verificación

    Se verificó correctamente:

- Docker Engine
- Docker CLI
- Docker Compose
- Docker Desktop

Comandos utilizados:

docker --version

docker compose version

docker info

docker run hello-world

## Problemas Encontrados

    ### Error 001

    Durante la instalación inicial DNF no encontró los paquetes Docker.

    Causa:

    El repositorio oficial de Docker no había sido agregado correctamente.

    Solución:

    Verificar `dnf repolist`, agregar nuevamente el repositorio oficial y repetir la instalación.

## Referencias

    - Documentación oficial de Docker
    - Documentación oficial de Fedora