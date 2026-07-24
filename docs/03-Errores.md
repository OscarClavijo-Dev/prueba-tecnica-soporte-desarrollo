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