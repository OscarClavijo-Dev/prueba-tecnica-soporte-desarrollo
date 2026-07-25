# Incidencia – Puerto 8000 ocupado y proceso Uvicorn persistente

## Contexto

Durante la ejecución de FastAPI mediante Uvicorn se presentó un conflicto con el puerto
8000, impidiendo iniciar una nueva instancia de la aplicación.

## Síntoma

Al ejecutar:

```bash
uvicorn app.main:app --reload

se obtuvo:

ERROR: [Error 98] Address already in use

# Diagnóstico

Se comprobó el puerto mediante:

ss -ltnp | grep :8000

El resultado mostró que el puerto estaba siendo utilizado por procesos asociados a
Uvicorn:

127.0.0.1:8000
uvicorn
python3

Posteriormente se identificaron los procesos mediante:

ps -fp 29753
ps -fp 32535

Se determinó que correspondían a la instancia anterior de Uvicorn ejecutada con:

uvicorn app.main:app --reload

## Causa

- El uso de --reload genera un proceso de supervisión y un proceso encargado de ejecutar
la aplicación. La instancia anterior no se había detenido correctamente y continuaba
manteniendo el puerto 8000 abierto.

Como consecuencia, una nueva instancia de Uvicorn no podía realizar el bind sobre
el mismo puerto.

## Resolución

- Inicialmente se intentó finalizar los procesos mediante:

kill <PID>

Como los procesos continuaron activos, se realizó una terminación forzada:

kill -9 <PID>

Posteriormente se verificó nuevamente el puerto:

ss -ltnp | grep :8000

La validación correcta consiste en que no exista ningún proceso escuchando en dicho
puerto antes de iniciar nuevamente FastAPI.

## Validación

Una vez liberado el puerto se inició nuevamente:

uvicorn app.main:app --reload

Posteriormente se validará el servicio mediante HTTP utilizando curl.