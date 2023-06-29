from flask import Blueprint

app_views = Blueprint('routes', __name__, url_prefix='/api/v1')

from api.v1.views.member import *
from api.v1.views.book import *
from api.v1.views.librarian import *
