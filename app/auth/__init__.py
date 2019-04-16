#  a blueprint that will handle all our application authentication requests
from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views,forms

