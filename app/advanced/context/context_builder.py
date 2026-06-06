def build_context(question,memory_state):
    context = {
        "current_question": question,
        "summary": memory_state["summary"],
        "recent_messages": memory_state["recent_messages"],
        "retrived_context": memory_state["retrived_context"],
    }
    return context
