from flask import Flask
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_cors import *

db = SQLAlchemy()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'

from app.models import Message, Comment, Post,Tag,Friend,User


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app)

    app.after_request(after_request)
    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    from .api import create_blueprint
    app.register_blueprint(create_blueprint())

    return app

def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')

    response.headers['Access-Control-Allow-Origin'] = '*'
    return response




