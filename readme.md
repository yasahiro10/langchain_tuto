# Langchain Tutorial
This tutorial is LangChain for LLM Application Development.
## Introduction
langchain is an opensource development framework for LLM applications.

key features: 
- Python and Javascript packages
- Focused on compostion and modularity
- Modular components
- components:
    - Models
    - prompts
    - Indexes
    - Agents
    - Chains
## Models, Prompts, Output Parses:
```bash
!pip install python-dotenv
!pip install openai
!pip install langchain
pip install -U langchain-ollama

```
for thoses who want to use openai but in this tutorial i will use llama3.2:3b (with ollama)
```bash
import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']
#############################################
from langchain.chat_models import ChatOpenAI
# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
chat = ChatOpenAI(temperature=0.0, model=llm_model)
```
## Installation

```bash
# Example installation steps
pip install -r requirements.txt