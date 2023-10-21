from flask import Blueprint, request, jsonify
from flask import Flask, request, jsonify
import os
import openai

api_blueprint = Blueprint("api", __name__)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

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