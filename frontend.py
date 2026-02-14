import streamlit as st
import requests
st.set_page_config(page_title="Sarcastic Python Tutor", page_icon="🐍")
st.title("🐍 Sarcastic Python Tutor")
st.write("Ask me a Python question, and I'll answer... eventually and SARCASTICALLY.")


with st.form(key='my_form', clear_on_submit=True):
    user_input = st.text_input("Your Question:", placeholder="e.g., How do I write a loop?")
    submit_button = st.form_submit_button(label='Ask the Expert')

if submit_button:
    if user_input:
        with st.spinner("Thinking up a sarcastic result..."):
            try:
                #Send to FastAPI
                response = requests.post(
                    "http://127.0.0.1:8000/ask-agent/",
                    json={"user_text": user_input}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if "agent_response" in data:
                        answer = data["agent_response"]
                        st.success("Here is your answer:")
                        st.markdown(answer)
                    else:
                        # If "agent_response" is missing, show the error message
                        st.error(f"Backend Error: {data.get('error', 'Unknown Error')}")
                        
                else:
                    st.error(f"Error: {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error("🚨 The Backend Server is down!")
    else:
        st.warning("Please type a question first.")