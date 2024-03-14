from app import app, db
from flask import render_template, request, redirect, session
from models.models import Car, Mark, Modelcar
from helpers.helpers import *
from flask import jsonify
from werkzeug.utils import secure_filename
import os

# ...

UPLOAD_FOLDER = './static/images'


@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    marks = Mark.query.all()
    modelcars = Modelcar.query.all()
    if request.method == 'POST':
        mark_id = request.form.get('mark')
        model_id = request.form.get('model')
        price = request.form.get('price')
        description = request.form.get('description')
        year = request.form.get('year')
        mileage = request.form.get('mileage')
        engine = request.form.get('engine')
        power = request.form.get('power')
        color = request.form.get('color')
        fuel = request.form.get('fuel')
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(image_path)

        author_id = None
        if 'user' in session:
            author_id = session['user']

        mark = Mark.query.get(mark_id)
        model = Modelcar.query.get(model_id)

        new_car = Car(name=mark.name, model=model.name, price=price, description=description,
                      year=year, mileage=mileage, engine=engine, power=power, color=color, fuel = fuel, image_url=image_path, user_id=author_id)
        db.session.add(new_car)
        db.session.commit()

        return redirect('/')

    return render_template('add_car.html', marks=marks, models=modelcars)

@app.route('/get_models/<int:mark_id>', methods=['GET'])
def get_models(mark_id):
    mark = Mark.query.get(mark_id)
    models = [{'id': model.id, 'name': model.name} for model in mark.models]
    return jsonify(models)

