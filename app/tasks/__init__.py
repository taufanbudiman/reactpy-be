from flask import Blueprint

bp = Blueprint('task', __name__)

from app.tasks import routes
