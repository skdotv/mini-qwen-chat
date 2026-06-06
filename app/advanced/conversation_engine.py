# this is to build memory orchaestration, which will be used to manage the conversation state, including summary, recent messages, and retrieved messages.

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

from .context.memory_state import memory_state


llm = ChatOllama(
    model = "qwen2.5-coder:7b-instruct-q6_K"
)

def chat (prompt):
    recent_messages = memory_state["recent_messages"]
    recent_messages.append(HumanMessage(content=prompt))

    response = llm.invoke(recent_messages)
    recent_messages.append(AIMessage(content=response.content))
    return response.content
    