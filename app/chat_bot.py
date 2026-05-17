from langchain_ollama import (ChatOllama,OllamaEmbeddings)
from langchain_core.messages import (SystemMessage,HumanMessage, AIMessage)
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "chroma_db"
llm= ChatOllama(model="qwen2.5-coder:7b-instruct-q6_K")


#load embeddings model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

#load vector db 
vector_store = Chroma(persist_directory=str(DB_PATH), embedding_function=embeddings)

#create retriver
retriever = vector_store.as_retriever( search_kwargs={"k": 3} )


# store conversation history 
chat_history = []

template = """ 
    You are an AI assistant.

    Use the retrieved context to answer the question.
    If the context contains relevant information,
    answer using it.
    If context is insufficient,
    you may use your own knowledge and clearly mention that.
    Conversation History:
    {history}
    Retrived Context:
    {context}
    Current question:
    {question} 
"""

prompt_template = ChatPromptTemplate.from_template(template)

def without_rag(question):
    history = "\n".join(chat_history)
    normal_prompt = f"""
    You are a helpful AI assistant.
    Conversation History:
    {history}
    Current Question:
    {question}
     """
    response = llm.invoke(normal_prompt)
    chat_history.append(HumanMessage(content=question))
    chat_history.append(AIMessage(content=response.content))
    return response.content


def with_rag(question):
    docs = retriever.invoke(question) 
    context = "\n\n".join([doc.page_content for doc in docs])
    history = "\n".join([f"{msg.__class__.__name__} : {msg.content}" 
    for msg in chat_history
    ])
    
    final_prompt = prompt_template.invoke({ "history":history, "context":context, "question":question})
    response = llm.invoke(final_prompt)
    # save your message to history
    chat_history.append(HumanMessage(content=question))
    # send full convesation
    response = llm.invoke(chat_history)
    # save AI response to history
    chat_history.append(AIMessage(content=response.content))
    return response.content


def ask_llm(question: str):
    use_rag = should_use_rag(question)
    if not use_rag:
        return without_rag(question)
        
    return with_rag(question)

def stream_llm(prompt: str):
    history = "\n".join(chat_history)
    use_rag = should_use_rag(prompt)
    if not use_rag:
        yield "🧠 Using LLM Knowledge...\n\n"
        final_prompt = f"""
        You are a helpful AI assistant.
        Conversation History:
        {history}
        Current Question:
        {prompt}
         """
    else:
        yield "📚 Retrieving From Documents...\n\n"
        docs = retriever.invoke(prompt)        
        context = "\n\n".join([doc.page_content for doc in docs])
        final_prompt = prompt_template.invoke({"history":history, "context":context, "question":prompt})    
        
    full_response = ""
    for chunk in llm.stream(final_prompt):
        token = chunk.content
        full_response += token 
        yield token 

        chat_history.append(f"User: {prompt}" )
        chat_history.append(f"AI: {full_response}") 

  

def should_use_rag(question: str):
    router_prompt = f"""
        You are a routing AI.
        Determine if this question requires
        retrieving information from uploaded documents.
        Answer ONLY:
        YES
        or
        NO
        Question:
        {question}
    """
    response = llm.invoke(router_prompt).content.strip().upper()
    print(f"#### FROM ROUTING MODEL {response} #####")

    return "YES" in response