from flask import Flask
from sentiment import simple_page

#how to make a requirements.txt

app = Flask(__name__)

app.register_blueprint(simple_page)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(port=5000)

