from app import app, db
from flask import render_template, request, redirect, session
from models.models import Car, User, Modelcar, Mark, Country
import os
from helpers.helpers import *
STATIC_FOLDER = '/static'
page_views = {}

@app.route('/car/<int:car_id>', methods=['GET', 'POST'])
def car_details(car_id):
    if request.method == 'GET':
        car = Car.query.get(car_id)
        id_user = car.user_id
        views = page_views.get(car_id, 0)
        views += 1
        page_views[car_id] = views
        count_of_user_ads = count_user_ads(id_user)
        country = Country.query.all()
        return render_template('car_details.html', car=car, views=views, country=country, count_of_user_ads=count_of_user_ads)
    else:
        return redirect("/")


def extract_filename_from_path(path):
    return os.path.basename(path)

app.jinja_env.globals.update(extract_filename_from_path=extract_filename_from_path)