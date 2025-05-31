import openai

# 👉 Step 1: Replace this with your real API key
openai.api_key = "org-sDQityL2yvtFJkWfxRknU8JV"

# 👉 Step 2: Ask a simple question
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Prompt Engineering?"}
    ]
)

# 👉 Step 3: Print the response
print(response['choices'][0]['message']['content'])
