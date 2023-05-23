""" Main server file for the Book Review App """
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from book_forms import NewBookForm, EditBookForm

load_dotenv()

# create the database
db = SQLAlchemy()

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# connect to database
db.init_app(app)

Bootstrap(app)
app.config["SECRET_KEY"] = os.environ["secret_key"]


class Books(db.Model):
    """Create a Books table in the database"""

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(250), unique=True, nullable=False)
    book_author = db.Column(db.String(250), nullable=False)
    book_rating = db.Column(db.Float, nullable=False)
    book_review = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """Render the home page"""
    all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Render the add book page"""
    form = NewBookForm()
    if form.validate_on_submit():
        new_book = Books(
            book_name=form.book_name.data,
            book_author=form.book_author.data,
            book_rating=form.book_rating.data,
            book_review=form.book_review.data,
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    """Render the edit book page"""
    form = EditBookForm()
    if form.validate_on_submit():
        book_to_update = Books.query.get(book_id)
        book_to_update.book_rating = form.book_rating.data
        book_to_update.book_review = form.book_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    """Send a DELETE request to the database"""
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
