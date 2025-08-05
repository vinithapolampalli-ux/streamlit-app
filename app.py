import streamlit as st

st.title("My First Streamlit App 🚀")
st.write("Hello, GitHub + Streamlit World!")
name = st.text_input("name:")
if name:
    st.success(f"Welcome, {name}!")