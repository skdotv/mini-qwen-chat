from fastapi.responses import StreamingResponse
from fastapi import FastAPI
from pydantic import BaseModel
from chat_bot import ask_llm, stream_llm

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "Welcome to the Qwen2.5 Chat API"}

@app.post("/chat")
def chat(req: ChatRequest):
    return StreamingResponse(
        stream_llm(req.prompt),
        media_type="text/plain"
    )
