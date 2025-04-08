import streamlit as st
import pandas as pd
from shared import render_sidebar

st.set_page_config(layout="wide")

@st.cache_data
def get_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Błąd połączenia z spreadsheets")
        return None

st.title("Wyzwanie ciągu Fibonacciego!")

sheet_url = "https://docs.google.com/spreadsheets/d/1JSTgwT8d623FTplInB7ByzFzoABZc6iCllKzS4oUais/gviz/tq?tqx=out:csv&gid=1425276992"
df = get_data(sheet_url)

st.write("Osoby, które ukończyły bieg na pozycji odpowiadającej liczbie w ciągu Fibonacciego:")
heigh = min(915,38*len(df))
st.dataframe(df, height=heigh, use_container_width=False, hide_index= True)

render_sidebar()