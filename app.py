import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Define the LLM outside the function
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

def model_response(query, chat_history):
    template = """You're a helpful and friendly assistant engaged in a natural conversation.

Previous Chat Context:
{chat_history}

User's Current Question:
{user_question}

Respond in a clear, friendly, and conversational manner. Provide helpful and concise information that directly addresses the user's question or continues the flow of the conversation."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", "{user_question}")
    ])

    # Properly construct the chain
    chain = (
        RunnablePassthrough.assign(
            chat_history=lambda x: x["chat_history"],
            user_question=lambda x: x["user_question"]
        )
        | prompt 
        | llm 
        | StrOutputParser()
    )

    return chain.stream({
        "chat_history": chat_history,
        "user_question": query
    })
    
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    
st.set_page_config(page_title="Streaming LLM using Gemini", page_icon='🎶')

st.title("Streaming LLM")

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("human"):
            st.markdown(message.content)
    else:
        with st.chat_message("Ai"):
            st.markdown(message.content)

user_input = st.chat_input('Your Message')
if user_input is not None and user_input != "":
    st.session_state.chat_history.append(HumanMessage(user_input))
    
    with st.chat_message("user"):
        st.markdown(user_input)
        
    with st.chat_message("assistant"):
        ai_response = st.write_stream(model_response(query=user_input, chat_history=st.session_state.chat_history))
    st.session_state.chat_history.append(AIMessage(ai_response))