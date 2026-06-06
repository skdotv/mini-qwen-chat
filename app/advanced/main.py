from fastapi import FastAPI
from pydantic import BaseModel

from .conversation_engine import chat


app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str


@app.post("/chat-summary")
def chat_summary(req: ChatRequest):
    response = chat(req.prompt)
    return {"response": response}