from langchain_ollama import ChatOllama

class SummaryMemory:
    def __init__(self, model="qwen2.5-coder:7b-instruct-q6_K", summary_trigger_messages=10):
    
        self.summary_trigger_messages = (summary_trigger_messages)
        self.llm = ChatOllama(model=model)
    
    def should_summarize(self,messages):
        return (len(messages) >= self.summary_trigger_messages)

    def summarize(self, messages):

        conversation = "\n".join([msg.content for msg in messages])
        prompt = f""" 
                    you are mainitaining a conversation memory. 
                    Extract: 
                    - user facts 
                    - goals 
                    - preferences
                    - decisions 
                    - important topics/informations

                    Create a concise memory. 

                    Conversation:
                    {conversation}

                    """
        
        response = self.llm.invoke(prompt)
        return response.content
    
    def update_summary(self, memory_state, summary):
        memory_state["summary"] = summary