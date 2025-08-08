import streamlit as st
from shared_data import load_data

st.set_page_config(page_title="Area Chart", page_icon="📉")

df = load_data()

st.markdown("## 📉 Area Chart - Sales Trend by Product")
st.area_chart(df, x='Pname', y='Psales')
