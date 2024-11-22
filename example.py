import streamlit as st

# Streamlit interface
st.title("Chatbot - DataPal")
st.write("Welcome! Ask me anything.")

# User input
user_input = st.text_input("You:")

# Display chatbot response
if st.button("Send"):
    st.write(f"DataPal: Sorry, I don't have a response yet for '{user_input}'!")

