from fastapi import FastAPI
from src.schemas.user_data import UserData

import joblib
import pandas as pd

app = FastAPI(
    title="PIM5 - API de Predicción",
    version="1.0.0",
    description="API inicial para disponibilizar un modelo de Machine Learning."
)

# Cargar modelo entrenado
model = joblib.load("src/models/model.joblib")

@app.get("/")
def root():

    return {
        "message": "API funcionando correctamente"
    }

@app.get("/health")
def health():

    return {
        "status": "ok"
    }

@app.post("/predict")
def predict(data: UserData):

    # Convertir datos a DataFrame
    features = pd.DataFrame([{
        "edad_cliente": data.edad_cliente,
        "salario_cliente": data.salario_cliente,
        "capital_prestado": data.capital_prestado,
        "plazo_meses": data.plazo_meses
    }])

    # Predicción
    prediction = model.predict(features)[0]

    return {
        "prediction": int(prediction)
    }