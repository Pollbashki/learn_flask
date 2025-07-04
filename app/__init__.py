# -*- coding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=Config.MIGRATIONS_DIR)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models