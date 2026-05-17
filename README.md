# Mini Qwen Chat 🤖

An interactive, AI-powered chatbot built with local LLM orchestration. This project leverages **Qwen 2.5** (running locally via Ollama) integrated through **LangChain** with a **FastAPI** backend and a **Gradio** web interface.

## 🌟 Key Features

* **Local AI Execution**: Runs `qwen2.5-coder:7b-instruct-q6_K` completely locally using Ollama, ensuring privacy and offline capability.
* **LangChain Orchestration**: Seamlessly handles prompt engineering, conversation memory, and model interactions.
* **FastAPI Backend**: A robust, high-performance API server providing real-time text streaming and well-documented endpoints.
* **Gradio Frontend UI**: A clean, intuitive chat interface for users to easily interact with the AI assistant.
* **Streaming Responses**: Real-time token streaming for a responsive conversational experience.

## 🎨 Interface Preview

<p align="center">
  <img src="app/assets/chat_ui.png" alt="Chat UI Demo" width="500"/>
</p>

## 🏗️ Architecture
```mermaid
graph TD
    A[Browser / Gradio UI] -->|HTTP Request| B[FastAPI Backend]
    B -->|Prompt| C[LangChain Orchestration]
    C -->|API Call| D[Ollama Server]
    D -->|Inference| E[Qwen2.5-Code Model]
    E -->|Stream Response| D
    D -->|Stream Response| C
    C -->|Stream Response| B
    B -->|Server-Sent Events| A
```

## 🚀 Getting Started

### Prerequisites

* **Python 3.8+**
* **Ollama**: Ensure you have [Ollama](https://ollama.ai/) installed on your machine.
* **Qwen Model**: Pull the required model via Ollama.
  ```bash
  ollama run qwen2.5-coder:7b-instruct-q6_K
  ```

### Installation

1. **Clone the repository** (or create the directory):
   ```bash
   git clone <your-repo-url>
   cd mini-qwen-chat
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install fastapi uvicorn langchain-ollama pydantic gradio
   ```

## 💻 Usage

The application is split into two parts: the backend API and the frontend UI.

### 1. Run the Backend (FastAPI)

Navigate to the `app` directory and start the server:

```bash
cd app
uvicorn main:app --reload
```

* The API will be available at: `http://127.0.0.1:8000`
* Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`

### 2. Run the Frontend (Gradio)

Open a new terminal, activate your virtual environment, and run the UI script:

```bash
cd app
python ui.py
```

* The Gradio interface will launch at: `http://127.0.0.1:7860`

## ✨ What This Project Covers

- ✅ **Local AI model** (Qwen 2.5 via Ollama)
- ✅ **LangChain orchestration** (Prompt engineering & Memory)
- ✅ **FastAPI backend** (Robust server with Streaming responses)
- ✅ **API routes** (Well-defined REST endpoints)
- ✅ **Swagger docs** (Interactive API documentation)
- ✅ **Real AI server** (Locally hosted without third-party API dependencies)

## 🔄 Data & Prompt Flow

Here is the step-by-step journey of a prompt from the user to the AI and back:

1. **User Input (Gradio UI)**: The user types a message in the Gradio web interface (`ui.py`).
2. **Frontend to Backend**: Gradio sends an HTTP POST request containing the prompt to the FastAPI backend (`main.py`) at the `/chat` endpoint.
3. **API Routing**: FastAPI receives the request, validates the JSON body using Pydantic, and calls the `stream_llm` function.
4. **LangChain Orchestration (`chat_bot.py`)**: 
   - The user's prompt is appended to the LangChain conversation history (Memory).
   - LangChain formats the entire conversation history (including the System Prompt) and sends it to the Ollama local server.
5. **Local Inference (Ollama + Qwen2.5)**: The Qwen model processes the prompt and starts generating a response token by token.
6. **Streaming Response**: 
   - As tokens are generated, LangChain streams them back to FastAPI.
   - FastAPI uses `StreamingResponse` to send these tokens back to the frontend in real-time.
7. **UI Update**: Gradio dynamically updates the chat interface as the text streams in, creating a typing effect.
8. **Memory Update**: Once generation is complete, the full AI response is saved back to LangChain's chat history for future context.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
