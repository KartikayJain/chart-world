import streamlit as st
from shared_data import load_data

st.set_page_config(page_title="Line Chart", page_icon="📈")

df = load_data()

st.markdown("## 📈 Line Chart - Sales Trend by Product")
st.line_chart(df, x='Pname', y='Psales')
