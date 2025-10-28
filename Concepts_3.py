import streamlit as st


st.title("Hleooo")

col1, col2 = st.columns(2)

with col1:
    if st.button("Press the Button."):
        st.success("Button Pressed")

with col2:
    input = st.text_input("Enter Your Name .")
    st.image("https://imgs.search.brave.com/yUG63VzDr4AG55A6AK2tM-YUYP6cuPAWyIpUX8RV8As/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi9saW9u/LXBvcnRyYWl0LXNh/dmFubmEtbW91bnQt/a2lsaW1hbmphcm8t/Mzg2MzgwMTYuanBn",width=200)
    if input:
        st.title(input)

side = st.sidebar.text_input("whats your Name.")

if side:
    st.sidebar.slider(f"Select Your Age {side}",0,100)
else:
    st.sidebar.success("WelCome To Tagruu World.")

with st.expander("Hello Piggsss."):
    st.write("""
            1.Dommma Tagruuuu
            2.Peot Tagruuuu
            3.Kall Tagruuu
    """)

st.markdown('### Shiglly Pig Alias Tukali Tagruuuu.')
st.markdown('> Dommma Peot')