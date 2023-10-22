from flask import Flask, jsonify, request
from dotenv import load_dotenv
from response import api_blueprint, generate_openai_response
from sentiment import sentiment_page
from response import create_initial_conversation, generate_openai_response

load_dotenv()
from response import create_initial_conversation, generate_openai_response

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/v1')  # Register the blueprint with a URL prefix
app.register_blueprint(sentiment_page)

@app.route('/openai', methods=['POST'])
def openai_endpoint():
    request_data = request.get_json()
    print(request_data)
    user_message = request_data['message']
    print(user_message)
    conversation = create_initial_conversation()
    response = generate_openai_response(user_message, conversation)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)