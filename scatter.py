import streamlit as st
from shared_data import load_data

st.set_page_config(page_title="Scatter Chart", page_icon="🎯")

df = load_data()

st.markdown("## 🎯 Scatter Plot - Price vs Quantity")
st.caption("Bubble color intensity represents total sales")

st.scatter_chart(df, x='Pquantity', y='Prate', color='Psales', size='Psales')
