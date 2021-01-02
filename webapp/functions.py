#!/usr/bin/env python3
import os
from PIL import Image
from werkzeug import secure_filename
import random, string
from flask import url_for,current_app
import json as m_json
import urllib
from PIL import Image
import os
from googlesearch import search

location_url = "https://latitudelongitude.org/in/"
def get_coordinates(place):
    place = str(place).split()[0]
    place = place.lower()
    rq = requests.get(location_url+place+"/")
    soup = BeautifulSoup(rq.content)
    data = soup.find_all('span')
    try:
        return data[0].string
    except Exception:
        return ""

def add_picture(image):

    file = secure_filename(image.filename)
    ext = file.split(".")[-1]
    rand = ''.join([random.choice(string.ascii_letters) for i in range(32)])
    filename  = rand+'.'+ext
    filepath = os.path.join(current_app.root_path,'static/place_images',filename)
    output_size = (720,720)
    pic = Image.open(image)
    pic.thumbnail(output_size)
    pic.save(filepath)
    return filename
