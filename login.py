from flask import Flask, Blueprint, render_template, abort, request, jsonify

login_page = Blueprint('login', __name__, template_folder='templates')

@login_page.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data provided!"}), 400

    username = data.get('username')
    password = data.get('password')