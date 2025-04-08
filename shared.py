import streamlit as st
import pandas as pd

def get_data(url):
    return pd.read_csv(url)

def render_sidebar():
    sheet_url = "https://docs.google.com/spreadsheets/d/1JSTgwT8d623FTplInB7ByzFzoABZc6iCllKzS4oUais/gviz/tq?tqx=out:csv&gid=1955630331" 
    try:
        now = get_data(sheet_url).iloc[0, 0]
    except Exception as e:
        now = "Błąd ładowania"

    with st.sidebar:
        st.markdown(f"🕒 **Aktualizacja:** {now}", unsafe_allow_html=True)
        st.markdown("🏃 [parkrun Ogród Saski, Lublin](https://www.parkrun.pl/ogrodsaski/)")
