import pandas as pd
import joblib

from explainability.fraud_reasoning import (
    generate_reason
)

print("Loading dataset...")

test_df = pd.read_parquet(
    "artifacts/feature_store/test_features.parquet"
)

TARGET = "label"

DROP_COLS = [
    "review_id",
    "user_id",
    "product_id"
]

# -----------------------------------
# PREPARE FEATURES
# -----------------------------------

X_test = test_df.drop(
    columns=DROP_COLS + [TARGET],
    errors="ignore"
)

X_test = X_test.replace(
    [float("inf"), -float("inf")],
    0
)

X_test = X_test.fillna(0)

object_cols = X_test.select_dtypes(
    include=["object"]
).columns

X_test = X_test.drop(
    columns=object_cols
)

# -----------------------------------
# MATCH TRAINING FEATURE COUNT
# -----------------------------------

expected_features = 36

X_test = X_test.iloc[:, :expected_features]

print("Feature shape:", X_test.shape)

print("Loading model...")

model = joblib.load(
    "artifacts/models/xgboost_model.pkl"
)

# -----------------------------
# XGBOOST COMPATIBILITY FIXES
# -----------------------------

compat_attrs = {
    "use_label_encoder": False,
    "gpu_id": -1,
    "predictor": "cpu_predictor"
}

for attr, value in compat_attrs.items():

    if not hasattr(model, attr):
        setattr(model, attr, value)
        
print("Generating predictions...")

preds = model.predict(X_test)

probs = model.predict_proba(X_test)[:, 1]

test_df["prediction"] = preds
test_df["fraud_probability"] = probs

print("Generating fraud explanations...")

test_df["fraud_reasons"] = test_df.apply(
    generate_reason,
    axis=1
)

output_cols = [
    "review_id",
    "fraud_probability",
    "prediction",
    "fraud_reasons"
]

available_cols = [
    c for c in output_cols
    if c in test_df.columns
]

explanations_df = test_df[
    available_cols
]

print(explanations_df.head())

explanations_df.to_parquet(
    "artifacts/explanations/local_explanations.parquet"
)

print("Local explanations generated.")