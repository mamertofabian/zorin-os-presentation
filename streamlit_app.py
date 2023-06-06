import streamlit as st
from streamlit_chat import message

from utils import ask_bot

# ------------------------------------------------------------------
# Save history

# This is used to save chat history and display on the screen
if 'answer' not in st.session_state:
    st.session_state['answer'] = []

if 'question' not in st.session_state:
    st.session_state['question'] = []

st.title("What question do you have for Zorin OS?")
prompt = st.text_input("Your question")

if prompt:
    response = ask_bot(prompt)
    st.empty()

    # Add the question and the answer to display chat history in a list
    # Latest answer appears at the top
    st.session_state.question.insert(0, prompt)
    st.session_state.answer.insert(0, response)

    # Display the chat history
    for i in range(len( st.session_state.question)) :
        message(st.session_state['question'][i], is_user=True)
        message(st.session_state['answer'][i], is_user=False)
