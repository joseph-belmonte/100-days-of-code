""" Main server file for the Book Review App """
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from book_form import BookForm


app = Flask(__name__)
Bootstrap(app)


all_books = []

load_dotenv()
app.config["SECRET_KEY"] = os.environ["secret_key"]


@app.route("/")
def home():
    """Render the home page"""
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Render the add page"""
    form = BookForm()
    if form.validate_on_submit():
        # append the entry as a dictionary to the list of books
        all_books.append(
            {
                "book_name": form.book_name.data,
                "book_author": form.book_author.data,
                "book_rating": form.book_rating.data,
                "book_review": form.book_review.data,
            }
        )
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(port=8000, debug=True)

cursor.execute(
    "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
)
