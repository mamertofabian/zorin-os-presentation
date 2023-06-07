import os

import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import streamlit as st

# from main import init_env_vars
# init_env_vars()

openai.api_key = st.secrets["OPENAI_API_KEY"]
# For LangChain
os.environ["OPENAI_API_KEY"] = openai.api_key

db = FAISS.load_local('index', OpenAIEmbeddings())
retriever = db.as_retriever(search_type='similarity', search_kwargs={'k': 4})


def get_sources(result):
    source_urls = []
    for document in result['source_documents']:
        url = document.metadata['source'].replace("website/", "https://")
        if url not in source_urls:
            source_urls.append(url)

    return source_urls


def ask_bot(question):
    chat_history = []
    qa = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(temperature=0), retriever=retriever, verbose=True,
                                               return_source_documents=True)

    return qa({"question": question, "chat_history": chat_history})
