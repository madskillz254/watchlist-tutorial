#blueprints are just instances or different versions of the same app,ie you can create a user view and an admins dashboard .same app different views
from flask import Blueprint
main = Blueprint('main',__name__) #blueprint class takes in two arguments name of blueprint and the __name__ variable to find the location of the variable #this is initialising the blueprint
from . import views,error  #done to prevent circular dependencies

