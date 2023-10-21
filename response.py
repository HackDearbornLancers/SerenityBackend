import openai

# Replace with your OpenAI API key
api_key = 'YOUR_API_KEY_HERE'
openai.api_key = api_key

def generate_openai_response(message):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=message,
            max_tokens=50,
            n=1,
            stop=None
        )

        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)