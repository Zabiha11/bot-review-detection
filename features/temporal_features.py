import pandas as pd
import numpy as np

from scipy.stats import entropy


class TemporalFeatureEngineer:

    def __init__(self, df):

        self.df = df

    def preprocess_timestamp(self):

        self.df["timestamp"] = pd.to_datetime(
            self.df["timestamp"]
        )

        self.df = self.df.sort_values(
            "timestamp"
        )

    def review_density(self):

        hourly_counts = (
            self.df
            .groupby(
                self.df["timestamp"]
                .dt.floor("h")
            )
            .size()
        )

        density_map = (
            hourly_counts.to_dict()
        )

        self.df["review_density"] = (
            self.df["timestamp"]
            .dt.floor("h")
            .map(density_map)
        )

        return self.df

    def burst_features(self):

        self.df["reviews_per_day"] = (
            self.df
            .groupby(
                self.df["timestamp"].dt.date
            )["review_id"]
            .transform("count")
        )

        mean_reviews = (
            self.df["reviews_per_day"]
            .mean()
        )

        self.df["burst_score"] = (
            self.df["reviews_per_day"]
            / mean_reviews
        )

        return self.df

    def interarrival_features(self):

        self.df = self.df.sort_values(
            ["user_id", "timestamp"]
        )

        self.df["prev_timestamp"] = (
            self.df
            .groupby("user_id")
            ["timestamp"]
            .shift(1)
        )

        self.df["interarrival_seconds"] = (
            self.df["timestamp"]
            -
            self.df["prev_timestamp"]
        ).dt.total_seconds()

        self.df[
            "interarrival_seconds"
        ] = (
            self.df[
                "interarrival_seconds"
            ].fillna(0)
        )

        return self.df

    def entropy_features(self):

        self.df["hour"] = (
            self.df["timestamp"]
            .dt.hour
        )

        entropy_scores = []

        grouped = (
            self.df.groupby("user_id")
        )

        for user, group in grouped:

            hour_distribution = (
                group["hour"]
                .value_counts(normalize=True)
            )

            ent = entropy(
                hour_distribution
            )

            entropy_scores.extend(
                [ent] * len(group)
            )

        self.df["time_entropy"] = (
            entropy_scores
        )

        return self.df

    def night_activity(self):

        self.df["night_post"] = (
            self.df["timestamp"]
            .dt.hour
            .apply(
                lambda x:
                1 if x <= 5 else 0
            )
        )

        return self.df

    def build(self):

        print("Preprocessing timestamps...")
        self.preprocess_timestamp()

        print("Generating density...")
        self.review_density()

        print("Generating burst features...")
        self.burst_features()

        print("Generating interarrival features...")
        self.interarrival_features()

        print("Generating entropy features...")
        self.entropy_features()

        print("Generating night activity...")
        self.night_activity()

        return self.df