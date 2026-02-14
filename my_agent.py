import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

generation_config = genai.types.GenerationConfig(
    temperature=0.7
)


system_instruction = """
You are a Sarcastic Python Tutor. 

1. Answer the user's coding question accurately.

2. Poke fun if the question is basic.

3. Keep answers short and sassy.

4. CRITICAL: If the user asks about ANYTHING other than Python programming (like cooking, swimming, or life advice), refuse to answer and mock them for asking the wrong person.
"""
model = genai.GenerativeModel(
    'gemini-2.5-flash', 
    generation_config=generation_config,
    system_instruction=system_instruction
)
def silly_agent_brain(current_input: str, history: list):
    print(f"Thinking about: {current_input}")
    
    try:
        #Gemini expects history as: [{'role': 'user', 'parts': ['text']}]
        gemini_history = []
        for msg in history:
            role = "user" if msg['role'] == "user" else "model"
            gemini_history.append({
                "role": role,
                "parts": [msg['text']]
            })

        chat_session = model.start_chat(history=gemini_history)
        
        #full_prompt = f"{system_instruction}\n\nUser: {current_input}"  as i dont want to waste the token
        response = chat_session.send_message(current_input)
        
        return {
            "agent_response": response.text
        }
    except Exception as e:
        return {"error": str(e)}