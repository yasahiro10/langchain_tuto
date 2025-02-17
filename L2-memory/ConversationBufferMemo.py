
from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversation.base import ConversationChain

model = ChatOllama(model='llama3.2:latest')
memory= ConversationBufferMemory()
conversation = ConversationChain(llm=model,memory=memory)
# print(conversation.predict(input="hi, my name is andrew"))
# print("############")
# print(conversation.predict(input='what is the most programming languages used in data'))
# print("############")
# print(conversation.predict(input="what is my name"))#Andrew, your name is Andrew! I remember we just started our conversation, and you told me that your name is Andrew. Don't worry, I'm here to help you with any questions or topics you'd like to discuss, so feel free to ask away!

print(memory.buffer) #print the whole conversation
print(memory.load_memory_variables({})) #{'history': ''}
memory.save_context({"input":'hi'},{"output":"what's up"}) #add context
print(memory.buffer)
print(memory.load_memory_variables({})) #{'history': "Human: hi\nAI: what's up"}
#################################
#ConversationBufferWindowMemory
from langchain.memory import ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(k=1)
memory.save_context({"input": "Hi"},
                    {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
print(memory.load_memory_variables({}))#{'history': 'Human: Not much, just hanging\nAI: Cool'} because k=1

#######################
#ConversationTokenBufferMemory
#pip install tiktoken
from langchain.memory import ConversationTokenBufferMemory
memory = ConversationTokenBufferMemory(llm=model, max_token_limit=50)
memory.save_context({"input": "AI is what?!"},
                    {"output": "Amazing!"})
memory.save_context({"input": "Backpropagation is what?"},
                    {"output": "Beautiful!"})
memory.save_context({"input": "Chatbots are what?"},
                    {"output": "Charming!"})
memory.load_memory_variables({})