import pandas as pd
import numpy as np
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.utils.class_weight import compute_class_weight
from sklearn.preprocessing import StandardScaler

from xgboost import XGBClassifier

from models.utils import (
    fit_pca,
    transform_pca,
    replace_embeddings
)

from models.config import (
    TARGET,
    DROP_COLS,
    PCA_COMPONENTS
)


print("Loading datasets...")

train_df = pd.read_parquet(
    "artifacts/feature_store/train_features.parquet"
)

val_df = pd.read_parquet(
    "artifacts/feature_store/val_features.parquet"
)

# ------------------------------------------------
# OPTIONAL PCA
# ------------------------------------------------

emb_cols = [
    c for c in train_df.columns
    if c.startswith("emb_")
]

if len(emb_cols) > 0:

    print("Embedding columns detected.")
    print("Running PCA reduction...")

    train_pca = fit_pca(
        train_df,
        emb_cols,
        PCA_COMPONENTS
    )

    val_pca = transform_pca(
        val_df,
        emb_cols
    )

    train_df = replace_embeddings(
        train_df,
        train_pca,
        emb_cols
    )

    val_df = replace_embeddings(
        val_df,
        val_pca,
        emb_cols
    )

else:

    print("No embedding columns found.")
    print("Skipping PCA reduction.")

# ------------------------------------------------
# TRAIN DATA
# ------------------------------------------------

X_train = train_df.drop(
    columns=DROP_COLS + [TARGET]
)


X_val = val_df.drop(
    columns=DROP_COLS + [TARGET]
)

X_train = X_train.replace([float("inf"), -float("inf")], 0)
X_val = X_val.replace([float("inf"), -float("inf")], 0)

X_train = X_train.fillna(0)
X_val = X_val.fillna(0)

object_cols = X_train.select_dtypes(include=["object"]).columns

X_train = X_train.drop(columns=object_cols)
X_val = X_val.drop(columns=object_cols)

bad_cols = [
    "community_id",
    "clustering_coeff"
]

X_train = X_train.drop(
    columns=[c for c in bad_cols if c in X_train.columns]
)

X_val = X_val.drop(
    columns=[c for c in bad_cols if c in X_val.columns]
)

y_train = train_df[TARGET].astype(int)
y_val = val_df[TARGET].astype(int)

print(X_train.dtypes)

print("\nObject columns:")
print(X_train.select_dtypes(include=["object"]).columns)

print("\nNull values:")
print(X_train.isnull().sum().sort_values(ascending=False).head(20))

print("Computing class weights...")

classes = np.array([0, 1])

weights = compute_class_weight(
    class_weight="balanced",
    classes=classes,
    y=y_train
)

important_cols = [
    "duplicate_review",
    "short_review",
    "extreme_rating",
    "user_review_count",
    "burst_score",
    "reviews_per_day",
    "avg_similarity",
    "max_similarity",
    "night_post"
]

for col in important_cols:

    if col in X_train.columns:

        X_train[col] *= 1.3
        X_val[col] *= 1.3
        
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

joblib.dump(
    scaler,
    "artifacts/models/scaler.pkl"
)

# ------------------------------------------------
# Logistic Regression
# ------------------------------------------------

print("Training Logistic Regression...")

class_weight_dict = {
    0: weights[0],
    1: weights[1]
}

log_model = LogisticRegression(
    max_iter=2000,
    random_state=42
)

log_model.fit(X_train, y_train)

log_preds = log_model.predict(X_val)

print(classification_report(
    y_val,
    log_preds
))

joblib.dump(
    log_model,
    "artifacts/models/logistic_regression.pkl"
)

# ------------------------------------------------
# Random Forest
# ------------------------------------------------

print("Training Random Forest...")

rf_model = RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight="balanced",
    n_jobs=-1,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_preds = rf_model.predict(X_val)

print(classification_report(
    y_val,
    rf_preds
))

joblib.dump(
    rf_model,
    "artifacts/models/random_forest.pkl"
)

# ------------------------------------------------
# XGBoost
# ------------------------------------------------

print("Training XGBoost...")

xgb_model = XGBClassifier(
    n_estimators=500,
    max_depth=5,
    learning_rate=0.03,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=1,
    reg_lambda=2,
    objective="binary:logistic",
    eval_metric="logloss",
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_probs = xgb_model.predict_proba(X_val)[:, 1]

xgb_preds = (xgb_probs > 0.40).astype(int)

print(classification_report(
    y_val,
    xgb_preds
))

joblib.dump(
    xgb_model,
    "artifacts/models/xgboost_model.pkl"
)

print("Training complete.")