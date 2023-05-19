from flask import Flask

app = Flask(__name__)


# @ is a decorator, which is a way to wrap a function
@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def bye_world():
    return "Goodbye!"


# is used to make a python file that is importable
# to other python files, as well as executable on its own

if __name__ == "__main__":
    app.run(debug=True)
