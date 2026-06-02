from pydantic import BaseModel


class FraudRequest(BaseModel):

    polarity: float = 0.0
    subjectivity: float = 0.0
    vader_score: float = 0.0

    char_count: int = 0
    word_count: int = 0
    avg_word_length: float = 0.0

    exclamation_count: int = 0
    uppercase_ratio: float = 0.0
    lexical_diversity: float = 0.0

    review_density: float = 0.0
    burst_score: float = 0.0
    interarrival_seconds: float = 0.0
    time_entropy: float = 0.0
    night_post: int = 0

    degree_centrality: float = 0.0
    pagerank: float = 0.0
    clustering_coeff: float = 0.0

    avg_similarity: float = 0.0
    anomaly_score: int = 0

    rating: float = 0.0
    duplicate_review: int = 0
    extreme_rating: int = 0
    short_review: int = 0
    user_review_count: int = 0
    max_similarity: float = 0.0
    reviews_per_day: float = 0.0
    same_day_spam: int = 0
    hour: int = 0

    pca_emb_0: float = 0.0
    pca_emb_1: float = 0.0
    pca_emb_2: float = 0.0
    pca_emb_3: float = 0.0
    pca_emb_4: float = 0.0
    pca_emb_5: float = 0.0
    pca_emb_6: float = 0.0
    pca_emb_7: float = 0.0
    pca_emb_8: float = 0.0
    pca_emb_9: float = 0.0