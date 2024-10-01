import pandas as pd
import numpy as np
import streamlit as st

st.title("This is a BMI Calc")
st.write("Calc stands for calculator for anyone wondering")

height = st.number_input("Enter your height (in meter): ",min_value=0.5,max_value=2.5,step=0.01)
weight = st.number_input("Enter your weight (in kilos): ",min_value=10,max_value=100,step=1)
happy = st.slider("How happy you are from 1 to 10",min_value=1,max_value=10,step=1)

def calculate_bmi(weight, height):
    if height > 0:
        bmi = weight / (height ** 2)
        return bmi
    return 0

