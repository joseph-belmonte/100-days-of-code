import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.environ["TMDB_API_KEY"]
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

##CREATE DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(app)


##CREATE TABLE
class Movie(db.Model):
    """Create Movie table"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


class FindMovieForm(FlaskForm):
    """FORM FOR SEARCHING MOVIES"""

    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class RateMovieForm(FlaskForm):
    """FORM FOR RATING MOVIES"""

    rating = DecimalField(
        "Your Rating Out of 10 e.g. 7.5",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=10, message="Rating must be between 0 and 10"),
        ],
    )
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/")
def home():
    """Renders the home page with all the movies in the database"""
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i, v in enumerate(all_movies):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """Renders the add movie page"""
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data

        response = requests.get(
            MOVIE_DB_SEARCH_URL,
            params={"api_key": TMDB_API_KEY, "query": movie_title},
            timeout=5,
        )
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    """Finds a movie from the movie database and adds it to the database"""
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(
            movie_api_url,
            params={"api_key": TMDB_API_KEY, "language": "en-US"},
            timeout=5,
        )
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))
    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    """Renders the edit page for rating and reviewing a movie"""
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    """Deletes a movie from the database"""
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
