#Executes multiple chains sequentially, passing the output of one as input to the next
#single input /output
from langchain.chains import SimpleSequentialChain, LLMChain
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
product = "Queen Size Sheet Set"
model = ChatOllama(model='llama3.2:latest',temperature = 0.9)
#prompt template 1
first_prompt = ChatPromptTemplate.from_template("What is the best name to describe a company that makes {product}?give one name")
#chain 1
chain_one = LLMChain(llm=model,prompt=first_prompt)

#prompt template 2
second_prompt = ChatPromptTemplate.from_template( "Write a 20 words description for the following company:{company_name}")
#chain 2
chain_two = LLMChain(llm=model, prompt=second_prompt)

overall_simple_chain = SimpleSequentialChain(chains=[chain_one,chain_two],verbose=True)
print(overall_simple_chain.run(product))

'''
> Entering new SimpleSequentialChain chain...
A simple yet elegant question!

I'd suggest the following name:

**Regalia Bedding**

"Regalia" implies grandeur, luxury, and majesty, which fits well with the idea of a queen-sized sheet set. It also has a regal, aristocratic tone to it, suggesting high-quality products fit for royalty.

What do you think?
Here is a 20-word description for Regalia Bedding:

"Experience luxury bedding fit for royalty, crafted with exquisite attention to detail and elegance, for the discerning sleeper's indulgence always."

> Finished chain.
Here is a 20-word description for Regalia Bedding:

"Experience luxury bedding fit for royalty, crafted with exquisite attention to detail and elegance, for the discerning sleeper's indulgence always."

'''