import streamlit as st
from api_client import predict_fraud

st.title("🔍 Fraud Review Analyzer")

st.markdown(
    "Enter fraud intelligence features"
)

col1, col2 = st.columns(2)

with col1:

    polarity = st.slider(
        "Polarity",
        -1.0,
        1.0,
        0.0
    )

    subjectivity = st.slider(
        "Subjectivity",
        0.0,
        1.0,
        0.5
    )

    vader_score = st.slider(
        "Vader Score",
        -1.0,
        1.0,
        0.0
    )

    char_count = st.number_input(
        "Character Count",
        0,
        1000,
        100
    )

    word_count = st.number_input(
        "Word Count",
        0,
        500,
        20
    )

    avg_word_length = st.slider(
        "Average Word Length",
        0.0,
        20.0,
        5.0
    )

    exclamation_count = st.number_input(
        "Exclamation Count",
        0,
        50,
        0
    )

    uppercase_ratio = st.slider(
        "Uppercase Ratio",
        0.0,
        1.0,
        0.0
    )

    lexical_diversity = st.slider(
        "Lexical Diversity",
        0.0,
        1.0,
        0.5
    )

with col2:

    review_density = st.slider(
        "Review Density",
        0.0,
        500.0,
        20.0
    )

    burst_score = st.slider(
        "Burst Score",
        0.0,
        10.0,
        1.0
    )

    interarrival_seconds = st.slider(
        "Interarrival Seconds",
        0.0,
        10000.0,
        500.0
    )

    time_entropy = st.slider(
        "Time Entropy",
        0.0,
        5.0,
        2.0
    )

    night_post = st.selectbox(
        "Night Post",
        [0, 1]
    )

    degree_centrality = st.slider(
        "Degree Centrality",
        0.0,
        1.0,
        0.1
    )

    pagerank = st.slider(
        "PageRank",
        0.0,
        1.0,
        0.1
    )

    clustering_coeff = st.slider(
        "Clustering Coefficient",
        0.0,
        1.0,
        0.1
    )

    avg_similarity = st.slider(
        "Average Similarity",
        0.0,
        1.0,
        0.3
    )

    anomaly_score = st.selectbox(
        "Anomaly Score",
        [0, 1]
    )

if st.button("Analyze Review"):

    payload = {
        "polarity": float(polarity),
        "subjectivity": float(subjectivity),
        "vader_score": float(vader_score),
        "char_count": int(char_count),
        "word_count": int(word_count),
        "avg_word_length": float(avg_word_length),
        "exclamation_count": int(exclamation_count),
        "uppercase_ratio": float(uppercase_ratio),
        "lexical_diversity": float(lexical_diversity),
        "review_density": float(review_density),
        "burst_score": float(burst_score),
        "interarrival_seconds": float(interarrival_seconds),
        "time_entropy": float(time_entropy),
        "night_post": int(night_post),
        "degree_centrality": float(degree_centrality),
        "pagerank": float(pagerank),
        "clustering_coeff": float(clustering_coeff),
        "avg_similarity": float(avg_similarity),
        "anomaly_score": int(anomaly_score)
    }

    result = predict_fraud(payload)

    if "prediction" not in result:

        st.error("Backend Error")

        st.write(result)

    else:

        st.subheader("Prediction Result")

        if result["prediction"] == 1:

            st.error("🚨 Fraudulent Review Detected")

        else:

            st.success("✅ Genuine Review")

        st.metric(
            "Fraud Probability",
            f"{result['fraud_probability']:.4f}"
        )

        st.subheader("Fraud Explanations")

        for reason in result["explanations"]:

            st.write(f"• {reason}")