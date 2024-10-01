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

if st.button("Calc BMI"):
    res = calculate_bmi(weight,height)
    st.write(f"Your BMI is: {res:.2f}")
    if res < 18.5 and happy < 5:
        st.write("you are skinny and sad as fuck")
    elif res < 18.5 and happy > 5:
        st.write("you are skinny and happy")

    elif (res < 18.5 and res > 24.9) and happy > 5:
        st.write("you are ok and sad as fuck")
    elif (res < 18.5 and res > 24.9) and happy < 5:
        st.write("you are ok and happy")

    elif res > 24.9 and happy > 5:
        st.write("you are fat and sad as fuck")
    elif res > 24.9 and happy < 5:
        st.write("you are fat happy")
