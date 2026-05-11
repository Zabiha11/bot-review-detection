import pandas as pd

from src.config.paths import (
    RAW_DIR,
    PROCESSED_DIR
)

from src.utils.validation import (
    validate_schema,
    validate_duplicates,
    validate_nulls
)


MASTER_COLUMNS = {
    "reviewID": "review_id",
    "reviewerID": "user_id",
    "restaurantID": "product_id",
    "reviewContent": "review_text",
    "rating": "rating",
    "date": "timestamp",
    "flagged": "label"
}


def load_reviews():

    train_df = pd.read_csv(
        RAW_DIR / "new_data_train.csv",
        sep="\t"
    )

    test_df = pd.read_csv(
        RAW_DIR / "new_data_test.csv",
        sep="\t"
    )

    print("Train Shape:", train_df.shape)
    print("Test Shape:", test_df.shape)

    # merge datasets
    df = pd.concat(
        [train_df, test_df],
        ignore_index=True
    )

    print("\nCombined Shape:", df.shape)

    # rename columns
    df = df.rename(columns=MASTER_COLUMNS)

    # keep only required columns
    df = df[list(MASTER_COLUMNS.values())]

    print("\nNormalized Columns:")
    print(df.columns)

    validate_schema(df)

    validate_duplicates(df)

    validate_nulls(df)

    return df


if __name__ == "__main__":

    df = load_reviews()

    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        PROCESSED_DIR /
        "reviews_raw.parquet"
    )

    df.to_parquet(
        output_path,
        index=False
    )

    print(f"\nSaved to {output_path}")