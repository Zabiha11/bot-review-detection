import pandas as pd

from src.config.paths import (
    PROCESSED_DIR
)


def build_users_table(df):

    users = df.groupby(
        "user_id"
    ).agg({
        "review_id": "count",
        "rating": "mean",
        "timestamp": ["min", "max"]
    })

    users.columns = [
        "review_count",
        "avg_rating",
        "first_review",
        "last_review"
    ]

    users = users.reset_index()

    # account age
    users["account_age_days"] = (
        users["last_review"]
        - users["first_review"]
    ).dt.days

    return users


def build_products_table(df):

    products = df.groupby(
        "product_id"
    ).agg({
        "review_id": "count",
        "rating": "mean"
    })

    products.columns = [
        "total_reviews",
        "avg_rating"
    ]

    products = products.reset_index()

    return products


def build_edges_table(df):

    edges = df[[
        "user_id",
        "product_id",
        "review_id",
        "timestamp",
        "label"
    ]]

    return edges


if __name__ == "__main__":

    df = pd.read_parquet(
        PROCESSED_DIR /
        "reviews_clean.parquet"
    )

    users = build_users_table(df)

    products = build_products_table(df)

    edges = build_edges_table(df)

    users.to_parquet(
        PROCESSED_DIR /
        "users.parquet",
        index=False
    )

    products.to_parquet(
        PROCESSED_DIR /
        "products.parquet",
        index=False
    )

    edges.to_parquet(
        PROCESSED_DIR /
        "edges.parquet",
        index=False
    )

    print("✅ Graph tables saved")