#!/usr/bin/python3
""" this module start a flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ return hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display hbnb"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def display_c_files(text):
    """Display the c + value of text var"""
    return 'C' + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    """ display python followed by the var """
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """ display n """
    return f'{} is a number'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
