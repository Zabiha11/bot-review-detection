import pandas as pd

print("Loading explanations...")

df = pd.read_parquet(
    "artifacts/explanations/local_explanations.parquet"
)

print("Preparing dashboard analytics...")

fraud_rate = df["prediction"].mean()

avg_probability = df[
    "fraud_probability"
].mean()

summary = {
    "total_reviews": len(df),
    "fraud_detected": int(df["prediction"].sum()),
    "fraud_rate": float(fraud_rate),
    "avg_fraud_probability": float(avg_probability)
}

summary_df = pd.DataFrame([summary])

summary_df.to_json(
    "artifacts/explanations/dashboard_summary.json",
    orient="records",
    indent=4
)

print(summary_df)