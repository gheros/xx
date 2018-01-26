from flask import Blueprint

ostck = Blueprint('ostck', __name__)

from . import views
