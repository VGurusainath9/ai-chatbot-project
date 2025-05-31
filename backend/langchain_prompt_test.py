from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.llms import Ollama


prompt = PromptTemplate(
    input_variables=["input"],
    template="Explain this: {input}"
)

llm = Ollama(model="mistral")

chain = LLMChain(llm=llm, prompt=prompt)

# Loop for dynamic input
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break
    response = chain.invoke({"input": user_input})
    print("Bot:", response['text'])

