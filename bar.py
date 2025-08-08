import streamlit as st
import plotly.express as px
from shared_data import load_data

st.set_page_config(page_title="Bar Chart", page_icon="📊")

df = load_data()

st.markdown("## 📊 Bar Chart - Product Sales Comparison")
fig = px.bar(df, x='Pname', y='Psales', title='Bar Chart of Product Sales',
             color='Psales', color_continuous_scale='Blues')
fig.update_layout(xaxis_title="Product Name", yaxis_title="Total Sales")

st.plotly_chart(fig, use_container_width=True)
