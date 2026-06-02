import os
import pandas as pd
import shap
import joblib
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

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

# -----------------------------
# PREPARE FEATURES
# -----------------------------

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

# -----------------------------
# IMPORTANT
# MATCH TRAIN FEATURE COUNT
# -----------------------------

expected_features = 36

X_test = X_test.iloc[:, :expected_features]

print("Feature shape:", X_test.shape)

print("Loading model...")

model = joblib.load(
    "artifacts/models/xgboost_model.pkl"
)

print("Sampling data...")

sample_data = X_test.sample(
    50,
    random_state=42
)

print("Building SHAP explainer...")

explainer = shap.TreeExplainer(model)

print("Generating SHAP values...")

shap_values = explainer.shap_values(
    sample_data
)

print("Creating explanations folder...")

os.makedirs(
    "artifacts/explanations",
    exist_ok=True
)

print("Generating summary plot...")

plt.figure(figsize=(10, 6))

shap.summary_plot(
    shap_values,
    sample_data,
    show=False
)

print("Saving plot...")

plt.savefig(
    "artifacts/explanations/shap_summary.png",
    bbox_inches="tight"
)

plt.close()

print("SHAP explanation complete.")