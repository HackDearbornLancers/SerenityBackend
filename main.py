from flask import Flask, jsonify, request
from dotenv import load_dotenv
from response import api_blueprint, generate_openai_response

load_dotenv()



app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/v1')  # Register the blueprint with a URL prefix

@app.route('/openai', methods=['POST'])
def openai_endpoint():
    request_data = request.get_json()
    response = generate_openai_response(request_data['message'])
    return jsonify({"response": response})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(port=5000)