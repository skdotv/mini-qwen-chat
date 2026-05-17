from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5-coder:7b-instruct-q6_K")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = llm.invoke(user_input)
    print("\nAI")
    print(response.content)
    print()
    

    


# python -> Langchain -> Ollama local server -> Qwen Model


# LangChain handles:

# * formatting
# * chat structure
# * providers
# * message types
# * memory
# * streaming
# * tools
# * agents

# project/

# │

# ├── venv/

# ├── app/

# │   ├── main.py

# │   ├── routes.py

# │   └── chatbot.py

# │

# ├── requirements.txt

# ├── README.md

# ├── .gitignore