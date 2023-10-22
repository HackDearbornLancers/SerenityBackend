from flask import Flask, jsonify, request
from dotenv import load_dotenv
from response import api_blueprint, generate_openai_response,create_initial_conversation
from sentiment import sentiment_page

load_dotenv()


app = Flask(__name__)
app.register_blueprint(api_blueprint)  # Register the blueprint with a URL prefix
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
    app.run(host= '0.0.0.0',port=8081)