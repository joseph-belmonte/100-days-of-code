""" This app is a cafe finder. It allows users to add cafes to the database and view them. """
import os
import csv
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from CafeForm import CafeForm
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["secret_key"]
Bootstrap(app)


# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
@app.route("/index")
def home():
    """Renders the home page."""
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    """Renders the add cafe page."""
    form = CafeForm()
    if form.validate_on_submit():
        new_data = [form.data[item] for item in form.data][:7]
        new_row = ",".join(new_data)
        with open("cafe-data.csv", newline="", encoding="utf8", mode="a") as csv_file:
            csv_file.write("\n" + new_row)
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    """Renders the cafes page."""
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
