# streamlit run chatbot.py

import streamlit as st
import requests

def invoke_XML():
    # Add Actors

    try:
        if "intentional_elements" in st.session_state:
            return ""
    except Exception as e:
            print(f'caught {type(e)}: e')

    return 'None'


st.header('Goal Modeling using ChatGPT', divider='rainbow')
# st.title("Goal Modeling using ChatGPT")


with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')

    chosen_temp = st.slider("Select Temperature",
                            0.0, 2.0, 0.80)
    st.write("Selected Temperature", chosen_temp)
    st.write("Selected LLM: gpt-3.5-turbo")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.intentional_elements = {}

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        url = ' http://127.0.0.1:5000'
        newPrompt = {"role": "user", "content": prompt}

        response = requests.post(url, json=newPrompt)

        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})