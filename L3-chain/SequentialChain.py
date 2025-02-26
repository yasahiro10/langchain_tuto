#More advanced than SimpleSequentialChain, allowing multiple inputs and outputs.
#Useful for complex workflows.
#(Multiple Inputs/Outputs)
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, SequentialChain
import pandas as pd
df = pd.read_csv('Data.csv')
review = df.Review[5]

model = ChatOllama(model="llama3.2:latest",temperature=0.9)

# prompt template 1: translate to english
first_prompt = ChatPromptTemplate.from_template(
    "Translate the following review to english:"
    "\n\n{Review}"
)
# chain 1: input= Review and output= English_Review
chain_one = LLMChain(llm=model, prompt=first_prompt,
                     output_key="English_Review")

second_prompt = ChatPromptTemplate.from_template(
    "Can you summarize the following review in 1 sentence:"
    "\n\n{English_Review}"
)
# chain 2: input= English_Review and output= summary
chain_two = LLMChain(llm=model, prompt=second_prompt,
                     output_key="summary")

# prompt template 3: translate to english
third_prompt = ChatPromptTemplate.from_template(
    "What language is the following review:\n\n{Review}"
)
# chain 3: input= Review and output= language
chain_three = LLMChain(llm=model, prompt=third_prompt,
                       output_key="language")

# prompt template 4: followup message
fourth_prompt = ChatPromptTemplate.from_template(
    "Write a follow up response to the following "
    "summary in the specified language:"
    "\n\nSummary: {summary}\n\nLanguage: {language}"
)
# chain 4: input= summary, language and output= followup_message
chain_four = LLMChain(llm=model, prompt=fourth_prompt,
                      output_key="followup_message")

# overall_chain: input= Review
# and output= English_Review,summary, followup_message
overall_chain = SequentialChain(
    chains=[chain_one, chain_two, chain_three, chain_four],
    input_variables=["Review"],
    output_variables=["English_Review", "summary","followup_message"],
    verbose=True
)
print(overall_chain(review))
'''
{'Review': "Je trouve le goût médiocre. La mousse ne tient pas, c'est bizarre.
 J'achète les mêmes dans le commerce et le goût est bien meilleur...\nVieux lot ou contrefaçon !?", 
 'English_Review': "Here's the translation of the review to English:\n\nI find the taste mediocre.
  The mousse doesn't hold up well, it's weird. I buy the same ones in stores and the taste is much 
  better...\n\nNote that the tone of the original French review is quite negative, but the translation
   tries to convey a sense of disappointment rather than outrage.", 
   'summary': 'The reviewer finds the 
   taste of the product mediocre and disappointing, citing that store-bought versions have a superior taste
    compared to this particular mousse.', 
    'followup_message': "Réponse de suivi :\n\nJe suis désolé d'apprendre 
    que notre crème moussée n'a pas réussi à impressionner dans votre cas. Cependant, je voudrais souligner qu'il existe 
    une grande variété de goûts et de préférences chez les consommateurs.\n\nBien que vous ayez déclaré que la saveur de
     notre crème moussée était médiocre et déçue, il est possible qu'elle vous plaise à d'autres personnes. De plus, 
     comme mentionné dans votre résumé, les versions de crème moussée acquises en magasin sont souvent considérées comme 
     étant supérieures en termes de saveur.\n\nJe vous propose de nous contacter pour discuter de vos expériences et de fournir 
     des informations supplémentaires sur les raisons pour lesquelles vous n'êtes pas satisfait du goût de notre produit.
      Nous sommes toujours ouverts à l'entendre et à faire des améliorations."}

'''