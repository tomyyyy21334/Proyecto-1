# Proyecto de API de control de logs

Este proyecto implementa una API REST simple para gestionar logs, desarrollada en Python utilizando FastAPI. Incluye tests, un Dockerfile y un workflow de CI/CD con GitHub Actions.

## Estructura del Proyecto

```
log-api-project/
├── app/
│   └── main.py             # Aplicación FastAPI
├── tests/
│   └── test_main.py        # Tests para la API
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # Workflow de GitHub Actions
├── Dockerfile              # Definición del contenedor Docker
├── requirements.txt        # Dependencias de Python
├── .dockerignore           # Archivos a ignorar por Docker
└── README.md               # Este archivo
```

## Requisitos

Para ejecutar este proyecto localmente, necesitarás:

*   Python 3.11+
*   pip (administrador de paquetes de Python)
*   Docker (para construir y ejecutar el contenedor)

## Configuración e Instalación Local

1.  **Clonar el repositorio:**

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd log-api-project
    ```

2.  **Crear un entorno virtual (opcional pero recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución de la API

Para iniciar la API localmente:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

La API estará disponible en `http://0.0.0.0:8000`. Puedes acceder a la documentación interactiva de Swagger UI en `http://0.0.0.0:8000/docs`.

## Endpoints de la API

*   **GET /**
    *   Descripción: Mensaje de bienvenida y estado de la API.
    *   Respuesta: `{"message": "Welcome to the Simple Log API", "status": "online"}`

*   **POST /logs/**
    *   Descripción: Crea un nuevo log.
    *   Cuerpo de la solicitud (JSON):
        ```json
        {
            "level": "INFO",
            "message": "Este es un mensaje de log de ejemplo."
        }
        ```
    *   Respuesta (JSON):
        ```json
        {
            "id": 1,
            "level": "INFO",
            "message": "Este es un mensaje de log de ejemplo.",
            "timestamp": "2023-10-27T10:00:00.000000"
        }
        ```

*   **GET /logs/**
    *   Descripción: Obtiene todos los logs o filtra por nivel.
    *   Parámetros de consulta: `level` (opcional, ej. `?level=ERROR`)
    *   Respuesta: Lista de objetos LogEntry.

*   **GET /logs/{log_id}**
    *   Descripción: Obtiene un log específico por su ID.
    *   Respuesta: Objeto LogEntry.

## Ejecución de Tests

Para ejecutar los tests unitarios:

```bash
pytest tests/
```

## Uso de Docker

### Construir la imagen Docker

Desde la raíz del proyecto:

```bash
docker build -t log-api:latest .
```

### Ejecutar el contenedor Docker

```bash
docker run -p 8000:8000 log-api:latest
```

La API estará disponible en `http://localhost:8000`.

## Integración Continua / Despliegue Continuo (CI/CD) con GitHub Actions

El archivo `.github/workflows/ci-cd.yml` define un pipeline de CI/CD que se ejecuta en cada `push` y `pull_request` a la rama `main`.

El workflow consta de dos jobs:

1.  **`test`**: Ejecuta los tests de Python usando `pytest`.
2.  **`build-docker`**: (Se ejecuta solo en `push` a `main` y después de que `test` haya pasado) Construye la imagen Docker de la aplicación.

### Cómo funciona el pipeline:

*   Al hacer `push` o `pull_request` a `main`, los tests se ejecutarán automáticamente.
*   Si los tests pasan (y es un `push` a `main`), la imagen Docker se construirá.
