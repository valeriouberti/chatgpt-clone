import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # This is the default and can be omitted
)

# Streamlit App Config
st.set_page_config(page_title="ChatGPT Clone", page_icon="🤖")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# App Title
st.title("🤖 ChatGPT Clone")

# Display Chat History
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if user_input := st.chat_input("Type your message here..."):
    # Display User Message
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Generate Response from OpenAI
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL_ID"),
            messages=st.session_state["messages"],
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"❌ Error: {e}"

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state["messages"].append({"role": "assistant", "content": reply})
