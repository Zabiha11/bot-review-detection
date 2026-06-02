import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📊 Fraud Analytics Dashboard")

try:

    df = pd.read_parquet(
        "artifacts/explanations/local_explanations.parquet"
    )

    fraud_rate = df["prediction"].mean()

    st.metric(
        "Fraud Detection Rate",
        f"{fraud_rate:.2%}"
    )

    fig = px.histogram(
        df,
        x="fraud_probability",
        nbins=20,
        title="Fraud Probability Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except Exception as e:

    st.error(str(e))