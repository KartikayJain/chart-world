import streamlit as st
import plotly.express as px
from shared_data import load_data

st.set_page_config(page_title="Treemap Chart", page_icon="📦")

df = load_data()

st.markdown("## 📦 Treemap - Sales Breakdown")
fig = px.treemap(df, path=['Pcategory', 'Pname'], values='Psales',
                 color='Psales', color_continuous_scale='Tealgrn')
st.plotly_chart(fig, use_container_width=True)
