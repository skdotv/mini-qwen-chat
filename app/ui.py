import gradio as gr 
from chat_bot import stream_llm

def chat(message, history):
    partial_message = ""
    for token in stream_llm(message):
        partial_message += token
        yield partial_message
    

interface = gr.ChatInterface(
    fn=chat,
    title="Mini Qwen Chat",
    description="Mini Qwen Hybrid RAG Chat"
)

if __name__ == "__main__":
    interface.launch()