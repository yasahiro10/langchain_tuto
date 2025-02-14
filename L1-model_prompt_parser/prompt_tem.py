#### Prompt Template

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
from langchain.prompts import ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_template(template_string)
print(prompt_template) #
print(prompt_template.messages)
print(prompt_template.messages[0])
print(prompt_template.messages[0].prompt.input_variables)
print(prompt_template.messages[0].prompt.input_variables)