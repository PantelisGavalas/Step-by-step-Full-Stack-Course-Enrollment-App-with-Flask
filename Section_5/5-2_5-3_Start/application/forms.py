from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


# Class for user Login Form
class LoginForm(FlaskForm):
    email   =   StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")
    

# Class for user Registration Form
class RegistraterForm(FlaskForm):
    email   =   StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    password_confirm = StringField("Confirm Password", validators=[DataRequired()])
    first_name = StringField("Firsy Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Register Now")
    