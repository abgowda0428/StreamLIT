import streamlit as st
import requests

st.title("Live Currency Converter.")

amount = st.number_input("Enter the input in INR .",min_value=1)

target_Currency = st.selectbox("Select Your Currency", ["USD","EUR","GBP","JPY"])

if st.button("Click Me"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_Currency]
        converted = (rate * amount,)
        st.success(f"{amount} INR = {converted[0]:.2f} {target_Currency}")
        # format specifier, will Activate through, : and we can specify roundUp Value
    else:
        st.write("Request Failed Due to Bad Server ,'404'....Try Againn ...")
