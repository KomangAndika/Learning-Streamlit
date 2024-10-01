import streamlit as st # type: ignore
import pandas as pd

st.write("Hellow world")
x = st.text_input("Favorite Food?")
st.write(f"Your fav food is: {x}")