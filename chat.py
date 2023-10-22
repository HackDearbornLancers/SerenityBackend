import openai

openai.api_key = "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"

prompt = input("Please enter a question or request: ")

result = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(result.choices[0].message.content)


