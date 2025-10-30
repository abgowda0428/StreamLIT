import streamlit as st
import pandas as pd 

st.title("Sales Dashboard")

file = st.file_uploader("Uplode Your File.",["csv","json"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Describe the Data")
    st.write(df.describe())