from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.


class CafeForm(FlaskForm):
    """Class is responsible for form logic"""

    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Location URL", validators=[DataRequired(), URL(message="Invalid URL")]
    )
    open_time = StringField("Open time", validators=[DataRequired()])
    close_time = StringField("Close time", validators=[DataRequired()])

    coffee = SelectField(
        "Coffee rating",
        choices=[
            ("0", "☕️"),
            ("1", "☕️☕️"),
            ("2", "☕️☕️☕️"),
            ("3", "☕️☕️☕️☕️"),
            ("4", "☕️☕️☕️☕️☕️"),
            ("5", "☕️☕️☕️☕️☕️☕️"),
        ],
        validators=[DataRequired()],
    )
    wifi = SelectField(
        "Wifi strength rating",
        choices=[
            ("0", "✘"),
            ("1", "💪"),
            ("2", "💪💪"),
            ("3", "💪💪💪"),
            ("4", "💪💪💪💪"),
            ("5", "💪💪💪💪💪"),
        ],
        validators=[DataRequired()],
    )
    power = SelectField(
        "Power outlet availability",
        choices=[
            ("0", "✘"),
            ("1", "🔌"),
            ("2", "🔌🔌"),
            ("3", "🔌🔌🔌"),
            ("4", "🔌🔌🔌🔌"),
            ("5", "🔌🔌🔌🔌🔌"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")
