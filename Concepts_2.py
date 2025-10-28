import streamlit as st

st.title("This is About Widget")

if st.button("Press Ready"):
    st.success("Done")

Condition_bx = st.checkbox("All Above Condition are ok")

if Condition_bx:
    st.success("Congralation You Achived")
else:
    st.write("Ntg is Selected")

a = st.selectbox("Selecte Any Of These :",["Animal","Cow","Bird","PIG"])

if a:
    st.success(a)
else:
    st.write("Nothing Selected")

Input = st.radio("Select Any of This",["Tagruu","pig","Big Sheep","TT"])

st.write(f"This is the Input, {Input} .")

sider_value = st.slider("Wts Your Level",10,50,15)

st.success(f"The selected value is {sider_value}")

Num_input = st.number_input("Select the Number",min_value=1,max_value=15,step=1)
if Num_input:
    st.success(Num_input)

Text_input = st.text_input("Type Your Name Here.")
if Text_input:
    st.success("Welcome BIG Peot Shrama,")

dob_of_sheep = st.date_input("Select Your Date.")
if  dob_of_sheep:
    st.write(f"Your DoB is,{dob_of_sheep}")
else:
    st.success("Welcome To Tgaruuu wold")