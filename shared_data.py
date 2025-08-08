# shared_data.py
import pandas as pd
import streamlit as st

def load_data():
    """Load and store dataframe in session_state to share across pages."""
    if "df" not in st.session_state:
        df = pd.read_csv('data.csv')
        df.insert(loc=5, column="Psales", value=df.eval('Pquantity*Prate'))
        st.session_state.df = df
    return st.session_state.df
