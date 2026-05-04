import streamlit as st
from model import get_response

st.title("🤖 NLP Chatbot")

user_input = st.text_input("Ask something:")

if user_input:
    response = get_response(user_input)
    st.write("Bot:", response)