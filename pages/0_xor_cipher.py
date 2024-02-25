import streamlit as st

st.header("Welcome to XOR Cipher!")
st.writer("What is your name")

txt_FNAME = st.text_input("FIRST NAME")
txt_LNAME = st.text_input("LAST NAME")

btn_submit = st.button("submit")

if btn_submit:
  st.write(f"Hello {txt_FNAME} {txt_LNAME}|")
