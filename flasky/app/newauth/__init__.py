from flask import Blueprint

newauth = Blueprint('newauth', __name__)

from . import views
