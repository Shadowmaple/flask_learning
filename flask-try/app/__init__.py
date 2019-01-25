from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

xyz = Flask(__name__)
#xyz为flask对象
db = SQLAlchemy(xyz)
migrate = Migrate(xyz, db)

from app import routes, models
xyz.config['SECRET_KEY'] = 'haha'


