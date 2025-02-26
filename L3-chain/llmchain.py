#Combines a prompt template with an LLM
import pandas as pd
df = pd.read_csv('Data.csv')

from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
model = ChatOllama(model='llama3.2:latest',temperature = 0.9)
#prompt template
prompt = ChatPromptTemplate.from_template("What is the best name to describe a company that makes {product}?")
#Combines a prompt template with an LLM
chain = LLMChain(llm = model,prompt = prompt)
product ="Queen Size Sheet Set"
print(chain.run(product))