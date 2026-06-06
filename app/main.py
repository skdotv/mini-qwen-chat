import json

from fastapi.responses import StreamingResponse
from fastapi import FastAPI
from pydantic import BaseModel
from app.chat_bot import stream_llm


def format_stream(prompt: str):
    for item in stream_llm(prompt):
        if isinstance(item, str):
            yield item
        else:
            yield json.dumps(item)

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "Welcome to the Qwen2.5 Chat API"}

@app.post("/chat")
def chat(req: ChatRequest):
    return StreamingResponse(
        format_stream(req.prompt),
        # stream_llm(req.prompt),
        media_type="text/plain"
    )
