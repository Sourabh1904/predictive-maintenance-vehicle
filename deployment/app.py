import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI(title="Vehicle Failure Prediction API")

# Load model and feature schema
model = joblib.load("xgb_model.pkl")
features = joblib.load("feature_columns.pkl")

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/predict")
def predict_failure(data: dict):
    # Convert input JSON to DataFrame
    df = pd.DataFrame([data])

    # Enforce same feature order as training
    df = df.reindex(columns=features, fill_value=0)

    # Prediction
    prob = model.predict_proba(df)[0][1]
    prediction = int(prob >= 0.5)

    return {
        "failure_risk": prediction,
        "failure_probability": round(float(prob), 3)
    }
