from flask import Blueprint
import os
import openai
from dotenv import load_dotenv

api_blueprint = Blueprint("api", __name__)
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
if api_key is None:
    raise EnvironmentError("API key not found in .env file")

def create_initial_conversation():
    # Create and return an initial conversation with a system message
    return [{"role": "system", "content": "You are an empathetic therapist."}] 

def generate_openai_response(message, conversation):
    conversation.append({"role": "user", "content": message})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0.6,  # Controls randomness in responses
            max_tokens=20,    # Limits the response length
            stop=None         # Ensure the response doesn't end prematurely
        )
        completion = response.choices[0].message["content"]
        conversation.append({"role": "assistant", "content": completion})  # Store assistant's response
        return completion

    except Exception as e:
        return str(e)
    