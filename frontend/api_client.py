import requests

BASE_URL = "http://127.0.0.1:8000"


def predict_fraud(payload):

    try:

        response = requests.post(
            f"{BASE_URL}/predict",
            json=payload
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }