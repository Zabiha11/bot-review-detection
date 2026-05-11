import pandas as pd

from src.config.paths import PROCESSED_DIR


def chronological_split(df):

    # sort by time
    df = df.sort_values("timestamp")

    total = len(df)

    train_end = int(0.8 * total)

    val_end = int(0.9 * total)

    train_df = df.iloc[:train_end]

    val_df = df.iloc[
        train_end:val_end
    ]

    test_df = df.iloc[val_end:]

    return train_df, val_df, test_df


if __name__ == "__main__":

    df = pd.read_parquet(
        PROCESSED_DIR /
        "reviews_clean.parquet"
    )

    train_df, val_df, test_df = (
        chronological_split(df)
    )

    train_df.to_parquet(
        PROCESSED_DIR /
        "train.parquet",
        index=False
    )

    val_df.to_parquet(
        PROCESSED_DIR /
        "val.parquet",
        index=False
    )

    test_df.to_parquet(
        PROCESSED_DIR /
        "test.parquet",
        index=False
    )

    print("✅ Train/Val/Test saved")