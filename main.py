from flask import Flask, jsonify, request
from dotenv import load_dotenv
from response import api_blueprint, generate_openai_response
<<<<<<< HEAD
from sentiment import simple_page
<<<<<<< Updated upstream
=======
from sentiment import sentiment_page
>>>>>>> 33c4ef162ed15b0982b175d3160e942e5d6d234e

load_dotenv()
=======
from response import create_initial_conversation, generate_openai_response
>>>>>>> Stashed changes

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/v1')  # Register the blueprint with a URL prefix
app.register_blueprint(sentiment_page)

@app.route('/openai', methods=['POST'])
def openai_endpoint():
    request_data = request.get_json()
<<<<<<< Updated upstream
    response = generate_openai_response(request_data['message'])
    return jsonify({"response": response})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
=======
    print(request_data)
    user_message = request_data['message']
    print(user_message)
    conversation = create_initial_conversation()
    response = generate_openai_response(user_message, conversation)
    return jsonify({"response": response})
>>>>>>> Stashed changes

if __name__ == "__main__":
    app.run(port=5000)