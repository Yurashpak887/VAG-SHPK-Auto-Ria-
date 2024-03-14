from app import api, db
from flask_restful import Resource
from models.models import Car
from flask import request, Response
from datetime import datetime

class CarResource(Resource):
    def get(self):
        cars = Car.query.all()
        car_list=[]
        for car in cars:
            car_list.append(car.serialize)
        return car_list

    def post(self):
        data = request.json
        current_datetime = datetime.now()
        car_add = Car(
            name=data.get('name'),
            model=data.get('model'),
            price=data.get('price'),
            year=data.get('year'),
            mileage=data.get('mileage'),
            engine=data.get('engine'),
            power=data.get('power'),
            color=data.get('color'),
            description=data.get('description'),
            image_url=data.get('image_url'),
            user_id=data.get('user_id'),
            registration_date=current_datetime
        )
        db.session.add(car_add)
        db.session.commit()
        return car_add.serialize


class CarSingleResource(Resource):
    def get(self,id):
        car = Car.query.get(id)
        return car.serialize

    def delete(self,id):
        try:
            car = Car.query.get(id)
            db.session.delete(car)
            db.session.commit()
            return Response("", status=204)
        except Exception:
            return Response("Car is not found", status=404)


api.add_resource(CarSingleResource, '/api/car/<int:id>')
api.add_resource(CarResource, '/api/car')
