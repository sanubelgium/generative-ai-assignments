import streamlit as st

st.title("Welcome to streamlit")
name = st.text_input("Enter your name")
st.button("Greet Me")
st.write(f"Hello, {name}!")