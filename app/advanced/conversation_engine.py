# this is to build memory orchaestration, which will be used to manage the conversation state, including summary, recent messages, and retrieved messages.

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

from .context.structured_memory import StructuredMemory

from .context.memory_state import memory_state
from .context.context_builder import build_context
from .context.context_prompt import build_prompt
from .context.summary_memory import SummaryMemory

summary_memory = SummaryMemory()  # Initialize summary memory with default settings
structured_memory = StructuredMemory()  # Initialize structured memory with default settings
llm = ChatOllama(
    model = "qwen2.5-coder:7b-instruct-q6_K"
)

def chat (prompt):
    structured_memory.process_message(prompt, memory_state)
    print("=== Updated Memory State ===")
    print(memory_state)
    recent_messages = memory_state["recent_messages"]
    recent_messages.append(HumanMessage(content=prompt))

    context = build_context(question = prompt, memory_state = memory_state)
    print("context: ", context)
    messsages = build_prompt(context)
    print("\n==== PRMPT ====\n")
    for msg in messsages:
        print(f"{msg.type}: {msg.content}\n")
        print()

    response = llm.invoke(messsages)
    recent_messages.append(AIMessage(content=response.content))
    if summary_memory.should_summarize(recent_messages):
        old_messages = recent_messages[:-4]
        summary = summary_memory.summarize(old_messages)
        summary_memory.update_summary(memory_state, summary)
        memory_state["recent_messages"] = recent_messages[-4:]
    return response.content
    