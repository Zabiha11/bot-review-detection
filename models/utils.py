import pandas as pd
import joblib

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def fit_pca(train_df, emb_cols, n_components=30):

    scaler = StandardScaler()

    train_scaled = scaler.fit_transform(
        train_df[emb_cols]
    )

    pca = PCA(
        n_components=n_components,
        random_state=42
    )

    train_pca = pca.fit_transform(train_scaled)

    joblib.dump(
        scaler,
        "artifacts/models/scaler.pkl"
    )

    joblib.dump(
        pca,
        "artifacts/models/pca.pkl"
    )

    return train_pca


def transform_pca(df, emb_cols):

    scaler = joblib.load(
        "artifacts/models/scaler.pkl"
    )

    pca = joblib.load(
        "artifacts/models/pca.pkl"
    )

    scaled = scaler.transform(
        df[emb_cols]
    )

    transformed = pca.transform(scaled)

    return transformed


def replace_embeddings(df, transformed, emb_cols):

    pca_df = pd.DataFrame(
        transformed,
        columns=[
            f"pca_emb_{i}"
            for i in range(transformed.shape[1])
        ]
    )

    df = df.drop(columns=emb_cols)

    df = pd.concat(
        [
            df.reset_index(drop=True),
            pca_df.reset_index(drop=True)
        ],
        axis=1
    )

    return df