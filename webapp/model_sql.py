import sqlite3 as sql
from werkzeug.security import generate_password_hash,check_password_hash
import os,sys
from datetime import datetime

def queryAll():
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir,"data.db")
    conn = sql.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM places")
    places = cur.fetchall()
    conn.close()
    return places

def insertPlaces(name,latitude,longitude,climate,language,description):
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir,"data.db")
    conn = sql.connect(database)
    cur = conn.cursor()
    cur.execute("INSERT INTO places(name,latitude,longitude,climate,language,description) VALUES (?,?,?,?,?,?)",(name,latitude,longitude,climate,language,description))
    conn.commit()
    conn.close()

def deletePlace(name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir,"data.db")
    conn = sql.connect(database)
    cur = conn.cursor()
    cur.execute("DELETE FROM places WHERE name=(?)",(name,))
    conn.commit()
    conn.close()


def retrievePlaces(name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir,"data.db")
    conn = sql.connect(database)
    cur = conn.cursor()
    name="%"+name+"%"
    cur.execute("SELECT * FROM places WHERE name LIKE (?) OR description LIKE (?)",(name,name))
    places = cur.fetchall()
    conn.close()
    return places

def updatePlace(name,latitude,longitude,climate,language,description):
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir,"data.db")
    conn = sql.connect(database)
    cur = conn.cursor()
    cur.execute("UPDATE places SET latitude=(?),longitude=(?),climate=(?),language=(?),description=(?) WHERE name=(?)",(latitude,longitude,climate,language,description,name))
    conn.commit()
    conn.close()

def retrievePlace(name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir,"data.db")
    conn = sql.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM places WHERE name=(?)",(name,))
    places = cur.fetchone()
    conn.close()
    return places

def insertReviews(name,username,rating,comments):
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir,"data.db")
    conn = sql.connect(database)
    cur = conn.cursor()
    cur.execute("INSERT INTO reviews(name,username,rating,comments,dates) VALUES (?,?,?,?,?)",(name,username,rating,comments,datetime.now()))
    conn.commit()
    conn.close()


def retrieveReviews(name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir,"data.db")
    conn = sql.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews WHERE name=(?) LIMIT 10",(name,))
    reviews = cur.fetchall()
    conn.close()
    return reviews
