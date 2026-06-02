import streamlit as st

from components.charts import create_graph


st.title(
    "🌐 Fraud Network Dashboard"
)

graph_path = create_graph()

with open(
    graph_path,
    "r",
    encoding="utf-8"
) as f:

    source_code = f.read()

st.components.v1.html(
    source_code,
    height=600
)