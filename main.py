from fastapi import FastAPI
from pydantic import BaseModel
from my_agent import silly_agent_brain

app = FastAPI()


#using a simple py list to store history.
chat_history = [] 

class UserQuery(BaseModel):
    user_text: str

@app.post("/ask-agent/")
def ask_agent(query: UserQuery):
    input_text = query.user_text
    
    #sending the new question+the OLD history to the list
    response_data = silly_agent_brain(input_text, chat_history)
    
    if "error" not in response_data:
        chat_history.append({"role": "user", "text": input_text})
        chat_history.append({"role": "model", "text": response_data["agent_response"]})
    
    return response_data

@app.post("/clear-memory/")
def clear_memory():
    chat_history.clear()
    return {"message": "Memory wiped!"}