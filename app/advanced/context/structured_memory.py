from langchain_ollama import ChatOllama
import json

class StructuredMemory:

    def __init__(self, model="qwen2.5-coder:7b-instruct-q6_K"):
        self.llm  = ChatOllama(model=model)


    def extract(self,conversation):
        prompt  = f"""
                  Extract structured memory. 
                  return ONLY valid JSON. 

                  Schema:
                  {{
                  "name":null,
                  "goal":null,
                  "project":null
                  }}

                  Conversation:
                  {conversation}
                   """
        response = self.llm.invoke(prompt)
        content = str(response.content).strip()
        if content.startswith("```json"):
            content  = (content.replace("```json","")).replace("```","").strip()

   
        print("\n=== RAW RESPONSE ===")
        print(response.content)
        print(content)
        try:
            # print(type(response.content))
            extracted = json.loads(str(content))
        except json.JSONDecodeError as e:
            extracted = {}
            print(f"Memory extraction failed: {e}")
            print(content)
        return extracted
    

    # why JSON and not free text: because structured memory needs deterministic updates.
    # json can be parsed, 
    # free text cannot be reliably merged.

    def merge(self, extracted_memory, memory_state):
        print(type(extracted_memory))
        name = extracted_memory.get("name")
        goal = extracted_memory.get("goal")
        project = extracted_memory.get("project")

        if name:
            memory_state["user_profile"]["name"] = name
        if goal:
            memory_state["goals"].append(goal)
        if project:
            memory_state["projects"].append(project)

    def process_message(self,message, memory_state):
        extract = self.extract(message)
        # update memory state
        self.merge(extract, memory_state)


