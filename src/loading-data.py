import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

data = pd.read_csv("/Users/komangandikawirasantosa/Learning-Streamlit/data/loan_data.csv")
st.write(data)

st.write("# Cool Chart init?")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a","b","c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)