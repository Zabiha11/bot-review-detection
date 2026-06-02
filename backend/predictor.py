import pandas as pd
import joblib

from backend.config import MODEL_PATH


print("Loading fraud model...")

model = joblib.load(MODEL_PATH)


def predict_fraud(data_dict):

    df = pd.DataFrame([data_dict])

    try:

        probability = model.predict_proba(df)[0][1]

    except Exception:

        probability = 0.0

    prediction = 0

    if probability > 0.30:

        prediction = 1

    # Rule-based fraud boosting
    if (
        data_dict["burst_score"] > 5
        or data_dict["avg_similarity"] > 0.9
        or data_dict["degree_centrality"] > 0.8
        or data_dict["night_post"] == 1
        or data_dict["anomaly_score"] == 1
    ):

        prediction = 1

        probability = max(
            probability,
            0.85
        )

    return {
        "prediction": int(prediction),
        "fraud_probability": float(probability)
    }