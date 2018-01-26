from flask import Blueprint

domain = Blueprint('domain', __name__)

from . import views

from ..models import Permission

