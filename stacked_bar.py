import streamlit as st
import plotly.express as px
from shared_data import load_data

st.set_page_config(page_title="Stacked Bar Chart", page_icon="📊")

df = load_data()

st.markdown("## 📊 Stacked Bar Chart - Sales by Product & Category")
fig = px.bar(df, x='Pcategory', y='Psales', color='Pname',
             title='Category-wise Sales',
             barmode='stack', color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig, use_container_width=True)
