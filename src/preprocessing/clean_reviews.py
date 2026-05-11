import pandas as pd
import re

from src.config.paths import PROCESSED_DIR


def clean_text(text):

    if pd.isna(text):
        return ""

    # lowercase
    text = text.lower()

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # remove weird unicode spaces
    text = text.strip()

    return text


def clean_reviews(df):

    print("Initial Shape:", df.shape)

    # remove duplicates
    df = df.drop_duplicates(
        subset=["review_id"]
    )

    # remove null critical fields
    df = df.dropna(subset=[
        "review_text",
        "timestamp",
        "user_id",
        "product_id"
    ])

    # clean text
    df["review_text"] = df[
        "review_text"
    ].apply(clean_text)

    # remove empty reviews
    df = df[
        df["review_text"].str.len() > 0
    ]

    # timestamp conversion
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    # remove invalid timestamps
    df = df.dropna(subset=["timestamp"])

    print("Final Shape:", df.shape)

    return df


if __name__ == "__main__":

    df = pd.read_parquet(
        PROCESSED_DIR /
        "reviews_raw.parquet"
    )

    cleaned_df = clean_reviews(df)

    cleaned_df.to_parquet(
        PROCESSED_DIR /
        "reviews_clean.parquet",
        index=False
    )

    print("\n✅ Clean dataset saved")