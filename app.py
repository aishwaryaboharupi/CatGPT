import streamlit as st
from cat_gpt import generate_meows

#Title 
st.title("CatGPT")

#Header
st.header("Generate Meows with Our AI-Powered Cat!")

#User input
user_input = st.text_input("Enter Your Prompt: ")

#Generate Meows Button
if st.button("Generate Meows"):
    #Generate Meows
    meows = generate_meows(user_input) 

    #Display Meows
    st.write(meows)