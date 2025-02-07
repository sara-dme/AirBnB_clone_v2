#!/usr/bin/python3
""" this module start a flask web application"""

from flask import Flask, render_template

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
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    """ display python followed by the var """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """ display n """
    return "{} is a number".format(n)


@app.route("/numbber_template/<int:n>", strict_slashes=False)
def display_template(n):
    """ display template if n is a num """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_even_odd_template(n):
    """ display html page with num n  """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
