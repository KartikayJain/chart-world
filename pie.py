import streamlit as st
import plotly.express as px
from shared_data import load_data

st.set_page_config(page_title="Pie Chart", page_icon="🥧")

df = load_data()

st.markdown("## 🥧 Pie Chart - Product Sales Distribution")
fig = px.pie(df, values='Psales', names='Pname', 
             title='Product Sales Share', 
             color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textinfo='percent+label')

st.plotly_chart(fig, use_container_width=True)
