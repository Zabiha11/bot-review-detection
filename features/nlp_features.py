import re
import pandas as pd
import numpy as np

from textblob import TextBlob
from vaderSentiment.vaderSentiment import (
    SentimentIntensityAnalyzer
)

vader = SentimentIntensityAnalyzer()


class NLPFeatureEngineer:

    def __init__(self, df):

        self.df = df

    def clean_text(self, text):

        text = str(text).lower()

        text = re.sub(
            r"http\S+",
            "",
            text
        )

        text = re.sub(
            r"[^a-zA-Z ]",
            "",
            text
        )

        return text.strip()

    def sentiment_features(self):

        self.df["clean_text"] = (
            self.df["review_text"]
            .apply(self.clean_text)
        )

        self.df["polarity"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                TextBlob(x)
                .sentiment
                .polarity
            )
        )

        self.df["subjectivity"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                TextBlob(x)
                .sentiment
                .subjectivity
            )
        )

        self.df["vader_score"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                vader
                .polarity_scores(x)["compound"]
            )
        )

        return self.df

    def stylometry_features(self):

        self.df["char_count"] = (
            self.df["clean_text"]
            .apply(len)
        )

        self.df["word_count"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                len(x.split())
            )
        )

        self.df["avg_word_length"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                np.mean(
                    [len(word)
                     for word in x.split()]
                )
                if len(x.split()) > 0
                else 0
            )
        )

        self.df["uppercase_ratio"] = (
            self.df["review_text"]
            .apply(
                lambda x:
                sum(
                    1
                    for c in str(x)
                    if c.isupper()
                )
                /
                max(len(str(x)), 1)
            )
        )

        self.df["exclamation_count"] = (
            self.df["review_text"]
            .apply(
                lambda x:
                str(x).count("!")
            )
        )

        self.df["lexical_diversity"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                len(set(x.split()))
                /
                max(len(x.split()), 1)
            )
        )

        return self.df

    def build(self):

        print("Building sentiment features...")
        self.sentiment_features()

        print("Building stylometry features...")
        self.stylometry_features()

        return self.df