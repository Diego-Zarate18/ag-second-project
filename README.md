# SIRUGA

Sistema Inteligente de Rutas Urbanas mediante Algoritmos Genéticos. Decide qué camiones de
recolección de basura se envían, a qué hora sale cada uno y qué ruta sigue, minimizando
tiempo de recorrido, costo y distancia, con tráfico por franja horaria.

El diseño completo (variables, objetivos, restricciones, base de conocimiento y operadores
genéticos) está en [`SIRUGA_grafo_conocimiento.json`](SIRUGA_grafo_conocimiento.json).

## Requisitos

- Python 3.11 o posterior (probado con 3.14)
- Git
- Docker Desktop con WSL2 (para Valhalla, a partir de la fase F4)

## Instalación en Windows (PowerShell)

```powershell
cd C:\ia-second-project
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Al activarlo, la línea de PowerShell empieza con `(.venv)`; instala siempre con el entorno activo.
Si PowerShell no deja activar el entorno, ejecuta una vez
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a intentarlo.

## Pruebas

```powershell
pytest
```

## Estructura

```text
backend/siruga/        código del sistema
backend/siruga/genetico/  algoritmo genético (F3)
backend/tests/         pruebas
frontend/              interfaz con Leaflet (F6)
valhalla/              configuración de Valhalla en Docker (F4)
datos/                 escenarios de prueba y de demostración
```

## Fases

| Fase | Contenido | Estado |
| --- | --- | --- |
| F0 | Preparación del repositorio | Completa |
| F1 | Modelo de datos y validaciones previas | Pendiente |
| F2 | Simulación del recorrido con tráfico | Pendiente |
| F3 | Algoritmo genético | Pendiente |
| F4 | Integración con Valhalla | Pendiente |
| F5 | API del backend | Pendiente |
| F6 | Interfaz con Leaflet | Pendiente |
| F7 | Pruebas de aceptación y escenario de demostración | Pendiente |
| F8 | Documentación y entrega | Pendiente |
