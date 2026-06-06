from langchain_core.messages import (SystemMessage, HumanMessage, AIMessage)

def build_prompt(context):
    messages = []
    system_prompt = """
                    You are a helpful assistant for answering questions.
                    Use the conversation summary when relevant.

                    Use recent conversation history to maintain continuity.

                    Answer clearly and accurately.

                    """

    messages.append(SystemMessage(content=system_prompt))
    summary = context["summary"]
    if summary:
        messages.append(SystemMessage(content=f"Conversation summary: {summary}"))
    messages.extend(context["recent_messages"])
    return messages



