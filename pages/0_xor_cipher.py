import streamlit as st

st.header("Welcome to XOR CIPHER")
st.write("What is your Name")

txt_FNAME = st.text_area("FIRST NAME")
txt_LNAME = st.text_area("LAST NAME")

btn_submit = st.button("submit")

if btn_submit:
  st.success(f"Hello {txt_FNAME"} {txt_LNAME"}|]
