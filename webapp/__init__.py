from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['SECRET_KEY'] ="whoismrrobot"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["MONGO_URI"] = "mongodb://localhost:27017/tourkarnataka"

mongo = PyMongo(app)

db = SQLAlchemy(app)
Migrate(app,db)
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from webapp.views import users
app.register_blueprint(users)
