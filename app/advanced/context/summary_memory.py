from langchain_core.messages import  HumanMessage, AIMessage


SUMMARY_TRIGGERS = 6

def should_summarize(messages):
    return len(messages) >= SUMMARY_TRIGGERS
