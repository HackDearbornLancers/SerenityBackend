from flask import Flask
from flask import Blueprint, render_template, abort, request, jsonify
from google.cloud import language_v2

simple_page = Blueprint('simple_page', __name__,template_folder='templates')

@simple_page.route("/s")
def hello_world():
    return "<p>Hello, World!</p>"

@simple_page.route("/sentiment", methods=['POST'])
def sentiment():
    if not request.json or 'text' not in request.json:
        return jsonify({"error": "Please provide text in JSON body"}), 400

    text_content = request.json['text']

    client = language_v2.LanguageServiceClient()

    document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT
    language_code = "en"
    document = {
        "content": text_content,
        "type_": document_type_in_plain_text,
        "language_code": language_code,
    }

    encoding_type = language_v2.EncodingType.UTF8
    response = client.analyze_sentiment(request={"document": document, "encoding_type": encoding_type})

    sentiment_score = response.document_sentiment.score
    sentiment_magnitude = response.document_sentiment.magnitude

    return jsonify({
        "sentiment_score": sentiment_score,
        "sentiment_magnitude": sentiment_magnitude
    })