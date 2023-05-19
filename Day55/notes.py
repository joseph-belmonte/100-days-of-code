""" 
Flask website to let user guess a number between 0 and 9
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return "Goodbye!"


# variable rules using <variable_name>
@app.route("/<name>")
def greet(name):
    return f"Hello {name + str(12)}!"


# you can chain multiple variables together
@app.route("/<name>/<int:number>")
def greet2(name, number):
    return f"Hello {name }! You are {number} years old!"


if __name__ == "__main__":
    app.run(port=8000, debug=True)  # debug=True to auto-reload server
