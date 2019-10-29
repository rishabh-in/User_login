# Registration Form
# Login Form

from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from myproject.models import User

class RegistrationForm(FlaskForm):

    email=StringField("Email",validators=[DataRequired(),Email()])
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired(),EqualTo("Confirm_password",message="Password do not match")])
    Confirm_password=PasswordField("Confirm Password",validators=[DataRequired()])
    submit=SubmitField("Register")

    def check_email(self,field):
        if User.string.filter_by(email=field.data).first():
            raise ValidationError("Your Email is already registered")

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already exist")

class Login(FlaskForm):

    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField("Login")