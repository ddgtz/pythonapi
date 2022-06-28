from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Must be at least 8 characters.')])
    email = StringField('Email', [Email(message='Invalid email.'), DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
