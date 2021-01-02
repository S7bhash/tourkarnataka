#!/usr/bin/env python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField,FloatField,IntegerField
from wtforms.validators import DataRequired, Email, EqualTo,Length,NumberRange
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed,FileRequired
from flask_login import current_user
from webapp.model import User


class SignUp(FlaskForm):
    username = StringField("Username",validators = [DataRequired()])
    city = StringField("city",validators=[DataRequired()])
    state = StringField("",validators=[DataRequired()])
    age = IntegerField("",validators=[DataRequired(message="Invalid input. Integer required"),NumberRange(min=18,max=85,message="Invalid Age...!")])
    occupation = StringField("",validators=[DataRequired()])
    email = StringField("E-mail",validators=[DataRequired(),Email(message="Invalid Email..!")])
    password = PasswordField("Password",validators=[DataRequired(),EqualTo('confirm',message="Password not matching..!"),Length(min=8,max=18,message="Password should be minimum of 8 characters with alpha-numericals.")])
    confirm = PasswordField("Confirm Password",validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class Login(FlaskForm):
    username  = StringField("",validators=[DataRequired()])
    password = PasswordField("",validators=[DataRequired()],render_kw={"placeholder":"Password","id":"ip"})
    submit = SubmitField("Login",render_kw={"placeholder":"Log In","id":"login","class":"btn btn-success"})

class ImageUpload(FlaskForm):

    image = FileField("Choose Image",[FileAllowed(['jpg','png','jpeg'],message="format not supported...!")])
    submit = SubmitField("Upload",render_kw={'id':"submit-upload"})


class SearchForm(FlaskForm):

    search = StringField("Search",validators=[DataRequired()],render_kw={'id':'search-space','placeholder':"Search",'class':"form-control mr-sm-2"})
    search_submit = SubmitField("Search",validators=[DataRequired()],render_kw={'id':'search','class':"btn btn-outline-success my-2 my-sm-0"})

class ReviewForm(FlaskForm):
    rating = FloatField("",validators=[DataRequired(message="Number Expected..!"),NumberRange(min=0,max=5,message="Expected value between 0.0 and 5.0 ..!")])
    comments = TextAreaField("",validators=[DataRequired()])
    submit = SubmitField("Submit",validators=[DataRequired()])

class AdminAdd(FlaskForm):
    name = StringField("",validators=[DataRequired()])
    latitude = StringField("",validators=[DataRequired()])
    longitude = StringField("",validators=[DataRequired()])
    language = StringField("",validators=[DataRequired()])
    climate = StringField("",validators=[DataRequired()])
    description = TextAreaField("",validators=[DataRequired()])
    submit = SubmitField("Upload",render_kw={'id':"submit-upload"})

class AdminDel(FlaskForm):
    name = StringField("",validators=[DataRequired()])
    submit = SubmitField("Delete",render_kw={'id':"submit-upload"})
