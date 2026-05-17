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





# ✅ Local AI model
# ✅ LangChain orchestration
# ✅ FastAPI backend
# ✅ API routes
# ✅ Swagger docs
# ✅ Real AI server


# Created backend server: 
# HTTP GET endpoint
# Chat endpoint 
# Basemodel validateds JSON automatically 
# Run backend: uvicorn app.main:app --reload
# source venv/bin/activate  to activate the venv

# CURRENT ARCHITECTURE
# Browser/User

#       ↓

# FastAPI

#       ↓

# chatbot.py

#       ↓

# LangChain

#       ↓

# Ollama

#       ↓

# Qwen2.5-Code


# step 2 :
# 1. Chat memory

# 2. Streaming responses

# 3. System prompts

# 4. Proper project structure

# 5. Frontend UI

# 6. RAG

# 7. Agents

# 8. MCP tools