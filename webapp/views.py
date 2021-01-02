from webapp import db,login_manager,mongo
from flask import render_template,url_for,flash,redirect,request,Blueprint,current_app
from flask_login import login_user, current_user, logout_user , login_required
from webapp.model import User,Rating
import requests
from bs4 import BeautifulSoup
from webapp.forms import SignUp,Login,ImageUpload,ReviewForm,SearchForm,AdminAdd,AdminDel
from webapp.functions import add_picture,get_coordinates
from webapp.model_sql import insertPlaces,insertReviews,retrievePlaces,retrieveReviews,retrievePlace,queryAll,insertPlaces,deletePlace,updatePlace
import smtplib
import random

from webapp.recommendation import find_relation

users = Blueprint('users',__name__)


@users.route("/report",methods=['GET','POST'])
def gokarana():
    place = [' Mirjan Fort','Kumta','Yana','Karwar','Yellapur']
    distance = [26,32,50,60,77]
    return render_template('report1.html',place=place,distance=distance)


@users.route('/signup',methods=['POST','GET'])
def signup():
    form = SignUp()
    if form.validate_on_submit():
        test_user=User.query.filter_by(username=form.username.data).first()
        print(test_user)
        if test_user:
            flash("Username registered...!")
            return redirect(url_for('users.signup'))
        if int(form.age.data) < 18:
            flash("You are under aged to create an account...!")
            return redirect(url_for('users.signup'))

        user = User(form.username.data,form.password.data,form.email.data,
                    form.city.data,
                    int(form.age.data),
                    form.occupation.data,
                    form.state.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for Registrating..!')
        return redirect(url_for('users.login',username=form.username.data))
    return render_template('signup.html',form=form)

@users.route('/login',methods=['GET','POST'])
def login():
    form =  Login()
    if form.validate_on_submit():
        if form.username.data == "admin-tourka" and form.password.data == "S7bhash":
            user = User.query.filter_by(username="admin-tourka").first()

            login_user(user)
            return redirect(url_for('users.admin'))

        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            if user.check_password(form.password.data):
                login_user(user)
                flash("Log In successful...!")
                return redirect(url_for('users.index'))
            else:
                flash("Wrong Password...!")
                return redirect(url_for('users.login'))
        else:
            flash("Username not found...!")
            return redirect(url_for('users.login'))
    return render_template('login.html',form=form)

@users.route('/admin',methods=["GET",'POST'])
#@login_required
def admin():
    form = AdminAdd()
    dele = AdminDel()
    if form.validate_on_submit():
        place = retrievePlace(form.name.data)
        if place:
            updatePlace(form.name.data,form.latitude.data,form.longitude.data,form.climate.data,form.language.data,form.description.data)
            flash("Updated successfully..!")
            return render_template('report.html',action="Update",action2="updated",name=form.name.data,lat=form.latitude.data,long=form.longitude.data,
                                climate=form.climate.data,description=form.description.data,language=form.language.data)
        insertPlaces(form.name.data,form.latitude.data,form.longitude.data,form.climate.data,form.language.data,form.description.data)
        flash(form.name.data + " successfully added...!")
        return render_template('report.html',action="Update",action2="added",name=form.name.data,lat=form.latitude.data,long=form.longitude.data,
                                climate=form.climate.data,description=form.description.data,language=form.language.data)
    if dele.validate_on_submit():
        place = retrievePlace(dele.name.data)
        if place:
            print(place)
            deletePlace(dele.name.data)
            flash(dele.name.data + " successful deleted..!")
            return render_template('report.html',action="Delete",action2="deleted",name=place[0],lat=place[1],long=place[2],
                                    climate=place[3],description=place[5],language=place[4])
        else:
            flash("No such place in record to delete...!")
            return redirect(url_for('users.admin'))
    return render_template('admin.html',form=form,dele=dele)


@users.route('/',methods= ['GET','POST'])
#@login_required
def index():
    search = SearchForm()
    if search.validate_on_submit():
        sent = str(search.search.data)
        word_list = sent.split()
        results = []
        for x in word_list:
            places = retrievePlaces(x)
            if places is not None:
                for place in places:
                    results.append(place)
        return render_template('results.html',results=results,name=search.search.data)
    return render_template('index.html',form=search,current_user=current_user)


@users.route('/<name>',methods=['GET','POST'])
#@login_required
def place_info(name):
    pictures = ['']
    form = ReviewForm()
    imageform =ImageUpload()
    places = retrievePlace(name)
    reviews = retrieveReviews(name)
    images = list(mongo.db.images.find({"name":name}))
    lat=float(places[1][:-1])
    long=float(places[2][:-1])
    if form.validate_on_submit():
        rate=Rating(user_id=current_user.id,place=name,rating=float(form.rating.data))
        db.session.add(rate)
        db.session.commit()
        insertReviews(name,
                        current_user.username,
                        form.rating.data,
                        form.comments.data)
        recos_places=find_relation(name)
        flash("Your review successfully added...!")
        if len(recos_places)>0:
            recos=[]
            for i in recos_places:
                recos.append(retrievePlace(i))
            return render_template('recommendations.html',results=recos)
        else:
            return redirect(url_for('users.place_info',name=name))
    if imageform.validate_on_submit():
        file=''
        if imageform.image.data:
            file = add_picture(imageform.image.data)
            mongo.db.images.insert({"name":name,"image":file})
            flash("Image successfully uploaded....!")
            return redirect(url_for('users.place_info',name=name))

    return render_template('place.html',name=name,form=form,imageform=imageform,images=images,reviews=reviews,places=places,lat=lat,long=long)


@users.route("/logout",methods=['GET','POST'])
#@login_required
def logout():
    logout_user()
    flash("You are logged out...!")
    return redirect(url_for('users.login'))
