from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required, email

class UserLoginForm(FlaskForm):
    #email, password, submit attributes
    email = StringField('Email', validators = [data_required(), email()])
    password = PasswordField('Password', validators=[data_required()])
    submit_button = SubmitField()
