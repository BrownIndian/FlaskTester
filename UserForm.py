from flask import Flask,render_template, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField('Submit', description="Some shit")


class InfoForm(FlaskForm):
    fname = StringField("Firstname", validators=[DataRequired()])
    lname = StringField("Lastname",validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    submit = SubmitField('Submit')

