#we will use ollama to call llama3.2:1b
#its a local model
'''
from langchain_ollama import ChatOllama # or from langchain_ollama.llms import OllamaLLM
chat = ChatOllama(model='llama3.2:1b')
print(chat) # model='llama3.2:1b'
'''
from langchain_ollama import ChatOllama
def get_completion(prompt):
    model = ChatOllama(model='llama3.2:1b', options={'num_gpu': 1})
    response = model.invoke(prompt)
    return response.content

print(get_completion("what is langchain"))