from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object("config.Config")
app.secret_key = "blablabla"
app.static_folder = 'static'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
page_views = {}

with app.app_context():
    from routes import *

from models.models import Car
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
