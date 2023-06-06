import os

import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]
# For LangChain
os.environ["OPENAI_API_KEY"] = openai.api_key

db = FAISS.load_local('index', OpenAIEmbeddings())
retriever = db.as_retriever(search_type='similarity', search_kwargs={'k': 4})
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


def ask_bot(question):
    qa = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(temperature=0), retriever=retriever, memory=memory,
                                               verbose=False)
    result = qa({"question": question})
    return result['answer']
