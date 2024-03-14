from app import db
from datetime import datetime



class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    engine = db.Column(db.Numeric(precision=5, scale=2, asdecimal=False), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    fuel = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255))  # Колонка для збереження URL зображення
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('cars', lazy=True))
    registration_date = db.Column(db.DateTime, default=db.func.now())



    @property
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'model':self.model,
            'price':self.price,
            'year':self.year,
            'mileage':self.mileage,
            'engine':self.engine,
            'power':self.power,
            'color':self.color,
            'description':self.description,
            'image_url':self.image_url,
            'user_id':self.user_id
        }




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    registration_date = db.Column(db.DateTime, default=db.func.now())
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))


class Country(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    country = db.relationship('User', backref='country')



class Mark(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    models = db.relationship('Modelcar', backref='mark', lazy=True)


class Modelcar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    mark_id = db.Column(db.Integer, db.ForeignKey('mark.id'), nullable=False)