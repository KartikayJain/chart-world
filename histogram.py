import streamlit as st
import plotly.express as px
from shared_data import load_data

st.set_page_config(page_title="Histogram", page_icon="📊")

df = load_data()

st.markdown("## 📊 Histogram - Sales Distribution")
fig = px.histogram(df, x='Psales', nbins=10, title='Sales Frequency Distribution',
                   color_discrete_sequence=['#636EFA'])
st.plotly_chart(fig, use_container_width=True)
