
from flask import Blueprint
from .v1 import v1

def create_blueprint():
    api = Blueprint('api', __name__)

    v1.register(api)

    return api