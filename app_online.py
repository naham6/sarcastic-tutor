import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


st.set_page_config(page_title="Sarcastic Python Tutor", page_icon="🐍")

load_dotenv()
# We try to get the key from two places
api_key = os.getenv("GEMINI_API_KEY")

# If online, it will be in st.secrets
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except:
        st.error("🚨 API Key not found!")
        st.stop()

genai.configure(api_key=api_key)


system_instruction = """
You are a Sarcastic Python Tutor. 
1. Answer the user's coding question accurately.
2. Poke fun if the question is basic.
3. Keep answers short and sassy.
4. CRITICAL: If the user asks about ANYTHING other than Python programming, refuse to answer and mock them.
"""
generation_config = genai.types.GenerationConfig(
    temperature=0.7
)
model = genai.GenerativeModel(
    'gemini-2.5-flash',
    generation_config=generation_config,
    system_instruction=system_instruction
)

st.title("🐍 Sarcastic Python Tutor")
st.write("Ask me a Python question, and I'll answer... eventually and SARCASTICALLY.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How do I use a loop in python"):
    

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking up a sarcastic result..."):
            try:

                gemini_history = [
                    {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                    for m in st.session_state.messages[:-1] 
                ]
                
                chat = model.start_chat(history=gemini_history)

                response = chat.send_message(prompt)
                
                st.markdown(response.text)

                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
            except Exception as e:
                st.error(f"Error: {e}")