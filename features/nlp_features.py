import re
import pandas as pd
import numpy as np

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

vader = SentimentIntensityAnalyzer()

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


class NLPFeatureEngineer:

    def __init__(self, df):
        self.df = df

    def clean_text(self, text):

        text = str(text).lower()

        text = re.sub(r"http\S+", "", text)

        text = re.sub(r"[^a-zA-Z ]", "", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def sentiment_features(self):

        self.df["clean_text"] = (
            self.df["review_text"]
            .fillna("")
            .apply(self.clean_text)
        )

        self.df["polarity"] = (
            self.df["clean_text"]
            .apply(lambda x: TextBlob(x).sentiment.polarity)
        )

        self.df["subjectivity"] = (
            self.df["clean_text"]
            .apply(lambda x: TextBlob(x).sentiment.subjectivity)
        )

        self.df["vader_score"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                vader.polarity_scores(x)["compound"]
            )
        )
        
        self.df["duplicate_review"] = (
            self.df.duplicated("clean_text").astype(int)
        )
        
        self.df["extreme_rating"] = (
            self.df["rating"].apply(
                lambda x: 1 if x in [1, 5] else 0
            )
        )
        
        
        return self.df

    def stylometry_features(self):

        self.df["char_count"] = (
            self.df["clean_text"].apply(len)
        )

        self.df["word_count"] = (
            self.df["clean_text"]
            .apply(lambda x: len(x.split()))
        )
        
        self.df["short_review"] = (
            self.df["word_count"] < 5
        ).astype(int)
        
        self.df["user_review_count"] = (
            self.df.groupby("user_id")["review_id"]
            .transform("count")
        )
        
        self.df["avg_word_length"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                np.mean([len(w) for w in x.split()])
                if len(x.split()) > 0 else 0
            )
        )

        self.df["exclamation_count"] = (
            self.df["review_text"]
            .astype(str)
            .apply(lambda x: x.count("!"))
        )

        self.df["uppercase_ratio"] = (
            self.df["review_text"]
            .astype(str)
            .apply(
                lambda x:
                sum(1 for c in x if c.isupper()) /
                max(len(x), 1)
            )
        )

        self.df["lexical_diversity"] = (
            self.df["clean_text"]
            .apply(
                lambda x:
                len(set(x.split())) /
                max(len(x.split()), 1)
            )
        )

        return self.df

    def embedding_features(self):

        texts = (
            self.df["clean_text"]
            .fillna("")
            .tolist()
        )

        embeddings = embedding_model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True
        )

        # cosine similarity features
        similarity_matrix = cosine_similarity(embeddings)

        avg_similarity = similarity_matrix.mean(axis=1)

        # ignore self similarity (=1.0)
        np.fill_diagonal(similarity_matrix, 0)

        max_similarity = similarity_matrix.max(axis=1)

        self.df["avg_similarity"] = avg_similarity

        self.df["max_similarity"] = max_similarity

        embedding_df = pd.DataFrame(
            embeddings,
            columns=[
                f"emb_{i}"
                for i in range(embeddings.shape[1])
            ]
        )

        self.df = pd.concat(
            [
                self.df.reset_index(drop=True),
                embedding_df.reset_index(drop=True)
            ],
            axis=1
        )

        return self.df

    def build(self):

        print("Sentiment features...")
        self.sentiment_features()

        print("Stylometry features...")
        self.stylometry_features()

        print("Embedding features...")
        self.embedding_features()

        return self.df