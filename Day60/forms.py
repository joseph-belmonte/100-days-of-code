from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """Form for user to log in"""

    username = StringField(
        label="username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    password = PasswordField(label="password", validators=[DataRequired()])
    remember = BooleanField(label="remember me")
    submit = SubmitField("Log In")


class RegisterForm(FlaskForm):
    """Form for user to register"""

    username = StringField("name", validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Register")
