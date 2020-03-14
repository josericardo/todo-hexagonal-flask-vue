from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    with open('index.html') as f:
        return f.read()
