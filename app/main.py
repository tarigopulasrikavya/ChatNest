from fastapi import FastAPI, HTTPException
from app.chatbot import get_chatbot_response
from app.models import ChatRequest, ChatResponse
import os

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = await get_chatbot_response(request.message)
        print("Response from chatbot:", response)  # Debug print
        return ChatResponse(response=response)
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug print
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Welcome to the LLM-powered chatbot API!"}


# uvicorn app.main:app --reload
# http://127.0.0.1:8000/chat
# curl -X POST 'http://127.0.0.1:8000/chat' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"message": "Hello, how are you?"}'

# ps aux | grep uvicorn