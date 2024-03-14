from app import app, db
from flask import render_template, request, redirect, session, url_for, flash
from models.models import Car, User, Mark, Modelcar
from helpers.helpers import *
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/images'



@app.route('/user-dashboard', methods=['GET', 'POST'])
def get_info():
    if 'user' in session:
        user = User.query.get(session['user'])
        country=Country.query.all()
        sorted_cars = request.args.get('sort_by', default=None)
        cars = Car.query.filter_by(
            user_id=user.id).all()
        cars = get_sorted_cars(sorted_cars,cars)
        return render_template('user-dashboard.html', user=user, cars=cars, get_sorted_cars=get_sorted_cars, country=country)
    return redirect('/login')


@app.route('/delete-car/<int:car_id>', methods=['GET', 'POST'])
def delete_car(car_id):
    car = Car.query.get(car_id)
    if car.user_id == session['user']:
        db.session.delete(car)
        db.session.commit()
    return redirect(url_for('get_info'))


@app.route('/edit_car/<int:car_id>', methods=['GET', 'POST'])
def edit_car(car_id):
    marks = Mark.query.all()
    modelcars = Modelcar.query.all()
    car = Car.query.get(car_id)
    if car.user_id == session['user']:
        if request.method == 'POST':
            mark_id = request.form.get('mark')
            model_id = request.form.get('model')
            price = request.form.get('price')
            year = request.form.get('year')
            mileage = request.form.get('mileage')
            engine = request.form.get('engine')
            power = request.form.get('power')
            fuel = request.form.get('fuel')
            color = request.form.get('color')
            description = request.form.get('description')

            image = request.files['image']

            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image_path = os.path.join(UPLOAD_FOLDER, filename)
                image.save(image_path)
            else:
                image_path = car.image_url

            car.mark_id = mark_id
            car.model_id = model_id
            car.price = price
            car.year = year
            car.mileage = mileage
            car.engine = engine
            car.power = power
            car.fuel = fuel
            car.color = color
            car.description = description
            car.image_url = image_path
            db.session.commit()
            return redirect('/')

        return render_template('edit_car.html', car=car, marks=marks, models=modelcars)

    return redirect('/')


def extract_filename_from_path(path):
    return os.path.basename(path)

app.jinja_env.globals.update(extract_filename_from_path=extract_filename_from_path)