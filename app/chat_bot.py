from langchain_ollama import ChatOllama
from langchain_core.messages import (SystemMessage,HumanMessage, AIMessage)


llm= ChatOllama(model="qwen2.5-coder:7b-instruct-q6_K")

# store conversation history 
chat_history = [
    SystemMessage(
    content=""" 
    You are a Senior AI engineer and coding assitant.
    Explain concepts clearly and step by step.
    """
    ),
]

def ask_llm(prompt: str):

    # save your message to history
    chat_history.append(HumanMessage(content=prompt))

    # send full convesation
    response = llm.invoke(chat_history)

    # save AI response to history
    chat_history.append(AIMessage(content=response.content))
    return response.content

def stream_llm(prompt: str):
    # save your message 
    chat_history.append(HumanMessage(content=prompt)) 
    full_response = ""
    for chunk in llm.stream(chat_history):
        token = chunk.content
        full_response += token 
        yield token 

    # save ai response to history 
    chat_history.append(AIMessage(content=full_response)) 

    

