from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class loginform(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('sign in')
