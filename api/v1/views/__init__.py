from api.v1.views.index import *
from api.v1.views.books import *
from api.v1.views.members import *
from flask import Blueprint

app_views = Blueprint('routes', __name__, url_prefix='/api/v1')
