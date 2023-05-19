from flask import Flask
import random

app = Flask(__name__)


winning_number = random.randint(0, 9)


@app.route("/")
def hello_world():
    """
    Greeting page
    """
    return """<h1>Guess a number between 0 and 9</h1>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>
        """


@app.route("/<int:number>")
def guess(number):
    """
    Guessing routes
    """
    r1 = random.randint(0, 255)
    r2 = random.randint(0, 255)
    r3 = random.randint(0, 255)
    if number > winning_number:
        return f"""<h1 style='color: rgb({r1},{r2},{r3})'>Too high, try again!</h1>
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>
        """
    elif number < winning_number:
        return f"""<h1 style='color: rgb({r1},{r2},{r3})'>Too low, try again!</h1>
        <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>
        """
    else:
        return """<h1>You found me!</h1>
        <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>
        """


if __name__ == "__main__":
    # port 8000 to avoid conflict with other local apps
    # debug = True to auto-reload server on code changes
    app.run(port=8000, debug=True)
