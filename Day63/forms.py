""" Controls the forms for the app """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddMovie:
    """Creates a form for adding a movie"""

    title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Movie Year", validators=[DataRequired()])
    description = StringField("Movie Description", validators=[DataRequired()])
    rating = StringField("Movie Rating", validators=[DataRequired()])
    ranking = StringField("Movie Ranking", validators=[DataRequired()])
    review = StringField("Movie Review", validators=[DataRequired()])
    img_url = StringField("Movie Image URL", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class EditMovie:
    """Creates a form for editing a movie"""

    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Done")
