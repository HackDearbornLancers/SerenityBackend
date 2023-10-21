from flask import Flask
from flask import Blueprint, render_template, abort

#how to make a requirements.txt

simple_page = Blueprint('simple_page', __name__,template_folder='templates')


@simple_page.route("/s")
def hello_world():
    return "<p>Hello, World!</p>"