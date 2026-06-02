from fastapi import FastAPI

from backend.schemas import FraudRequest
from backend.predictor import predict_fraud
from backend.explain import generate_explanation


app = FastAPI(
    title="ReviewShield AI",
    description="Coordinated Bot Review Detection API",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "ReviewShield AI Backend Running"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(request: FraudRequest):

    data = request.dict()

    prediction = predict_fraud(data)

    explanations = generate_explanation(data)

    return {
        "prediction": prediction["prediction"],
        "fraud_probability": prediction["fraud_probability"],
        "explanations": explanations
    }