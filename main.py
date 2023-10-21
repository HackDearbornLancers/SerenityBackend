from flask import Flask, request, jsonify
from sentiment import simple_page
from response import generate_openai_response

app = Flask(__name__)

app.register_blueprint(simple_page)

@app.route('/openai', methods=['POST'])
def openai_endpoint():
    #request_data = request.get_json()
    #response = generate_openai_response(request_data['message'])
    #return jsonify({"response": response})
    response_data = {"message": "This is your API response."}
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(port=5000)

