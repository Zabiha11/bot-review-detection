import pandas as pd

from features.nlp_features import (
    NLPFeatureEngineer
)

from features.temporal_features import (
    TemporalFeatureEngineer
)

from features.graph_features import (
    GraphFeatureEngineer
)

from features.feature_fusion import (
    FeatureFusion
)


def run_pipeline(
    input_path,
    output_path
):

    print("Loading dataset...")

    df = pd.read_parquet(
        input_path
    )

    print("NLP pipeline...")
    df = NLPFeatureEngineer(df).build()

    print("Temporal pipeline...")
    df = TemporalFeatureEngineer(df).build()

    print("Graph pipeline...")
    df = GraphFeatureEngineer(df).build()

    print("Feature fusion...")
    df = FeatureFusion(df).build()

    print("Saving features...")

    df.to_parquet(
        output_path,
        index=False
    )

    print("✅ Feature engineering complete")


if __name__ == "__main__":

    run_pipeline(
        "data/processed/train.parquet",
        "artifacts/feature_store/train_features.parquet"
    )

    run_pipeline(
        "data/processed/val.parquet",
        "artifacts/feature_store/val_features.parquet"
    )

    run_pipeline(
        "data/processed/test.parquet",
        "artifacts/feature_store/test_features.parquet"
    )