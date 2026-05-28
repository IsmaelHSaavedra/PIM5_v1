import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

# Cargar dataset
df = pd.read_excel("Base_de_datos.xlsx")

# Variables predictoras
X = df[[
    "edad_cliente",
    "salario_cliente",
    "capital_prestado",
    "plazo_meses"
]]

# Variable objetivo
y = df["Pago_atiempo"]

# División train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Modelo
model = RandomForestClassifier(random_state=42)

# Entrenamiento
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Métrica
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")

# Guardar modelo
joblib.dump(model, "src/models/model.joblib")

print("Modelo guardado correctamente.")