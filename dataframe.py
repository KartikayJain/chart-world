import streamlit as st
from shared_data import load_data

st.set_page_config(page_title="Data Dashboard", page_icon="📑", layout="wide")

df = load_data()

st.markdown("## 📑 Product Sales Data Table")
st.markdown("<p style='color: grey;'>All calculations are done automatically, including total sales per product.</p>", unsafe_allow_html=True)

st.dataframe(df, use_container_width=True)
