#### Prompt Template

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
from Model_call import get_completion
from langchain.prompts import ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_template(template_string)

print(prompt_template) #input_variables=['style', 'text'] input_types={} partial_variables={} messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['style', 'text'], input_types={}, partial_variables={}, template='Translate the text that is delimited by triple backticks into a style that is {style}. text: ```{text}```\n'), additional_kwargs={})]
print(prompt_template.messages)#[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['style', 'text'], input_types={}, partial_variables={}, template='Translate the text that is delimited by triple backticks into a style that is {style}. text: ```{text}```\n'), additional_kwargs={})]
print(prompt_template.messages[0])#prompt=PromptTemplate(input_variables=['style', 'text'], input_types={}, partial_variables={}, template='Translate the text that is delimited by triple backticks into a style that is {style}. text: ```{text}```\n') additional_kwargs={}
print(prompt_template.messages[0].prompt.input_variables) #['style', 'text']

customer_style = """American English \
in a calm and respectful tone
"""
customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""
customer_message = prompt_template.format_messages(style=customer_style,text=customer_email)
print(customer_message[0]) #content="Translate the text that is delimited by triple backticks into a style that is American English in a calm and respectful tone\n. text: ```\nArrr, I be fuming that me blender lid flew off and splattered me kitchen walls with smoothie! And to make matters worse, the warranty don't cover the cost of cleaning up me kitchen. I need yer help right now, matey!\n```\n" additional_kwargs={} response_metadata={}
print(get_completion(customer_message))
#model response
'''I'm really upset because my blender lid flew off and damaged my kitchen walls with smoothie.
And to make things worse, the warranty doesn't cover the cost of cleaning up my kitchen. 
I was hoping we could help me out right now.'''