from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

app = Flask(__name__)
CORS(app)

# Prepare AI model
llm = ChatOllama(model="mistral")
prompt = PromptTemplate(
    input_variables=["input"],
    template="Answer clearly: {input}"
)
chain = LLMChain(llm=llm, prompt=prompt)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    response = chain.invoke({"input": user_message})
    return jsonify({"reply": response['text']})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
