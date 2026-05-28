# PIM5_v1 - API de predicción ML
Este repositorio sirve para trabajar en el Proyecto Integrador del Módulo 5 de la carrera de Data Science de Henry

API desarrollada con FastAPI para disponibilizar un modelo de Machine Learning entrenado con Scikit-Learn. El proyecto incluye entrenamiento del modelo, serialización con Joblib y despliegue mediante Docker.

## Tecnologías utilizadas

- Python
- FastAPI
- Scikit-Learn
- Docker
- Joblib
- Uvicorn

## Estructura del proyecto

```text
PIM5_v1/
│
├── src/
│   ├── api/
│   │   └── main.py
│   ├── models/
│   │   ├── modelo.joblib
│   │   └── train_model.py
│   └── schemas/
│       └── user_data.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── Base_de_datos.xlsx
```

## Instalación local

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Ejecución local

```bash
uvicorn src.api.main:app --reload --port 5000
```

## Construcción de imagen Docker

```bash
docker build -t pim5-api .
```

## Ejecución del contenedor

```bash
docker run -p 5000:5000 pim5-api
```
## Explicación de puertos Docker

### `-p 5000:5000`

El puerto 5000 del host se conecta al puerto 5000 interno del contenedor. La API queda accesible desde:

```text
http://127.0.0.1:5000
```

### `-p 8000:5000`

El puerto 8000 del host se conecta al puerto 5000 interno del contenedor. Aunque la API continúa ejecutándose en el puerto 5000 dentro del contenedor, externamente se accede mediante:

```text
http://127.0.0.1:8000
```

## Endpoint principal

### POST `/predict`

Ejemplo de JSON enviado al endpoint:

```json
{
  "edad_cliente": 50,
  "salario_cliente": 30000,
  "capital_prestado": 70000,
  "plazo_meses": 48
}
```

Ejemplo de respuesta:

```json
{
  "prediction": 1
}
```

## Swagger UI

La documentación interactiva de la API puede visualizarse desde:

```text
http://127.0.0.1:5000/docs
```

## Versionado

- v1.0.0:
  Estructura inicial del proyecto y análisis exploratorio.

- v1.0.1:
  Implementación de API FastAPI, serialización del modelo y despliegue mediante Docker.