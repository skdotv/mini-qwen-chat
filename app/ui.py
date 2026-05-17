import gradio as gr 
from chat_bot import ask_llm

def chat(message):
    return ask_llm(message)

interface = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="Mini Qwen Chat",
    description="Ask me anything about AI and coding!"
)

if __name__ == "__main__":
    interface.launch()