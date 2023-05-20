import os
from flask import Flask, render_template
from forms import LoginForm
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap

load_dotenv()

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = os.environ["APP_SECRET_KEY"]


@app.route("/")
def home():
    """Renders the home page."""
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Renders the login page."""
    form = LoginForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        # if the form has successfully been validated
        if form.username.data == "admin" and form.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
