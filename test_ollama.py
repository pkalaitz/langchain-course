from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:4b",  # Replace with a model from `ollama list`
    base_url="http://localhost:11434",
)

response = model.invoke("Hello! Explain what LangChain is in one sentence.")

print(response.content)