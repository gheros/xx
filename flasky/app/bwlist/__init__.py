from flask import Blueprint

bwlist = Blueprint('bwlist', __name__)

from . import views

from ..models import Permission

