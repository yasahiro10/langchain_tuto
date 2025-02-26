
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

#Conversation summary memory
from langchain.memory import ConversationSummaryBufferMemory
# create a long string
schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=model, max_token_limit=100)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"},
                    {"output": f"{schedule}"})
print(memory.load_memory_variables({}))
#{'history': 'System: The human says hello and asks what\'s on the schedule for the day.
# The AI responds with a casual "Not much" to match the human\'s tone,
# indicating that everything seems normal or uneventful.\n\nNew lines of conversation:\nHuman: Can you suggest something I
# could do today?\nAI: Actually, how about taking a walk outside?\n\nNew summary:\n\nThe human asks what\'s on the schedule
# for the day and responds with "Not much" after saying hello. The AI suggests doing something active like taking a walk outside
# to brighten up the day.\nAI: There is a meeting at 8am with your product team. You will need your powerpoint presentation prepared.
# 9am-12pm have time to work on your LangChain project which will go quickly because Langchain is such a powerful tool. At Noon, lunch
# at the italian resturant with a customer who is driving from over an hour away to meet you to understand the latest in AI. Be sure to
# bring your laptop to show the latest LLM demo.'}
