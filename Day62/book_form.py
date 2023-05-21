"""
Form logic for adding a new book
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    """Creates a book form that can add a new book to the database"""

    book_name = StringField("Book Name", validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    book_rating = SelectField(
        "Rating", choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]
    )
    book_review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit")
