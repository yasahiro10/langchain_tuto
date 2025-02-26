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

```
# LangChain Memory Types

LangChain provides several types of **memory** to help retain conversational context in applications using LLMs. Below is an overview of the key **memory types**:

## 1. ConversationBufferMemory
- Stores the full conversation history.
- Useful when maintaining the entire context is important.
- Example use case: Chatbots that need full recall of past interactions.

### Example:
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context({"input": "Hello"}, {"output": "Hi, how can I help?"})
print(memory.load_memory_variables({}))
```

---

## 2. ConversationBufferWindowMemory
- Keeps only the last `k` messages, reducing memory size.
- Useful when full history isn't needed but recent context matters.

### Example:
```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=2)
memory.save_context({"input": "Hello"}, {"output": "Hi, how can I help?"})
memory.save_context({"input": "What is LangChain?"}, {"output": "A framework for LLMs."})
memory.save_context({"input": "Tell me more"}, {"output": "It helps build AI applications."})

print(memory.load_memory_variables({}))  # Shows only the last 2 interactions
```

---

## 3. ConversationSummaryMemory
- Summarizes past interactions instead of storing full history.
- Useful when keeping memory concise while retaining key points.
- Uses an LLM (like GPT) to generate summaries.

### Example:
```python
from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
memory = ConversationSummaryMemory(llm=llm)

memory.save_context({"input": "I love AI!"}, {"output": "That's great!"})
memory.save_context({"input": "Tell me about LangChain"}, {"output": "It's a useful framework."})

print(memory.load_memory_variables({}))  # Shows a summarized version
```

---

## 4. ConversationEntityMemory
- Extracts and stores **key entities** (like names, dates, places) from conversations.
- Useful when tracking specific details about a user or topic.

### Example:
```python
from langchain.memory import ConversationEntityMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
memory = ConversationEntityMemory(llm=llm)

memory.save_context({"input": "My name is John and I live in Paris"}, {"output": "Nice to meet you, John!"})
print(memory.load_memory_variables({}))  # Shows extracted entities: {"John": "User's name", "Paris": "User's location"}
```

---

## 5. VectorStoreRetrieverMemory
- Stores conversation history in **a vector database** for **long-term memory**.
- Useful for applications that need to retrieve old conversations based on semantic meaning.

### Example:
```python
from langchain.memory import VectorStoreRetrieverMemory
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(["Hello, how are you?"], embedding=embeddings)
retriever = vectorstore.as_retriever()

memory = VectorStoreRetrieverMemory(retriever=retriever)
print(memory.load_memory_variables({}))  # Retrieves stored context
```

---

## Summary Table
| Memory Type                      | Use Case |
|-----------------------------------|---------|
| **ConversationBufferMemory**      | Store full history |
| **ConversationBufferWindowMemory** | Keep only recent `k` messages |
| **ConversationSummaryMemory**     | Summarize conversations dynamically |
| **ConversationEntityMemory**      | Track named entities like names & places |
| **VectorStoreRetrieverMemory**    | Long-term memory with vector search |
