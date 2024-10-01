import streamlit as st # type: ignore
import pandas as pd # type: ignore

data = pd.read_csv("/Users/komangandikawirasantosa/Learning-Streamlit/data/loan_data.csv")
st.write(data)