#! /usr/bin/env python3
from webapp import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
import random,string
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(64),nullable=False)
    city = db.Column(db.String(32))
    age = db.Column(db.Integer)
    state = db.Column(db.String(32))
    occupation = db.Column(db.String(64))

    def __init__(self,username,password,email,city,age,occupation,state):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.city = city
        self.age = age
        self.occupation = occupation
        self.state = state

    def check_password(self,password):
        return check_password_hash(self.password,password)


class Rating(db.Model):

    __tablename__="ratings"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer)
    place = db.Column(db.String(32))
    rating = db.Column(db.Float)

    def __init__(self,user_id,place,rating):
        self.user_id=user_id
        self.place=place
        self.rating=rating













