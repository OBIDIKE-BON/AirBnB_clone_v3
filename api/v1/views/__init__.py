from flask import Blueprint

if not True:
    from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
