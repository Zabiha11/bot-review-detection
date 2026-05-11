REQUIRED_COLUMNS = [
    "review_id",
    "user_id",
    "product_id",
    "review_text",
    "rating",
    "timestamp",
    "label"
]


def validate_schema(df):

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    print("✅ Schema validation passed")


def validate_duplicates(df):

    duplicates = (
        df["review_id"]
        .duplicated()
        .sum()
    )

    print(
        f"Duplicate review_ids: {duplicates}"
    )


def validate_nulls(df):

    print("\nNull values:")
    print(df.isnull().sum())