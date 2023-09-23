# app.py
from apply import Flask
from language import testcall

app = Flask(__name__)


@app.route('/get_translation/<text>')
def get_translation(text):
    return testcall(text)
