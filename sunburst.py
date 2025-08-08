import streamlit as st
import plotly.express as px
from shared_data import load_data

st.set_page_config(page_title="Sunburst Chart", page_icon="🌞")

df = load_data()

st.markdown("## 🌞 Sunburst Chart - Category & Product Sales")
fig = px.sunburst(df, path=['Pcategory', 'Pname'], values='Psales',
                  color='Psales', color_continuous_scale='Viridis',
                  title='Sales Breakdown by Category & Product')

st.plotly_chart(fig, use_container_width=True)
