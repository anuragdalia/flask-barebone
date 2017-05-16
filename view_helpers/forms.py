# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
from flask_wtf import RecaptchaField, FlaskForm
from wtforms.validators import *
from wtforms import StringField, PasswordField, DateField, SubmitField, HiddenField


class SignupForm(FlaskForm):
    csrf = True
    name = StringField("Name", validators=[DataRequired(), Regexp('^[a-z ]+$', message="Can contain only letters and a space")])
    dob = DateField("Date of Birth", format='%d/%m/%Y', validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    contactno = StringField("Contact No - included country code", validators=[DataRequired()])
    recaptcha = RecaptchaField("Are you a hooman too? Hi!")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
