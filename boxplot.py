import streamlit as st
import plotly.express as px
from shared_data import load_data

st.set_page_config(page_title="Box Plot", page_icon="🔍")

df = load_data()

st.markdown("## 🔍 Box Plot - Price Distribution by Category")
fig = px.box(df, x='Pcategory', y='Prate', points="all",
             color='Pcategory', title='Price Variation Across Categories')
st.plotly_chart(fig, use_container_width=True)
