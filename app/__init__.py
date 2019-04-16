from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  #an extension that helps us manage the user authentication system

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'        #this attribute provides different security levels and by setting it to strong will monitor the changes in a user's request header and log the user out.
login_manager.login_view = 'auth.login'           #We prefix the login endpoint with the blueprint name because it is located inside a blueprint.

def create_app(config_name):
    '''
this function allows us to add the configurations to the app effectively
'''
    app = Flask(__name__)

    # Creating the app configurations..to allow access to the environment variables
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions  We call the init_app() on an extension to complete on their initialization.
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate') # url_prefix argument that will add a prefix to all the routes registered with that blueprint.

        # setting config
    from .requests import configure_request
    configure_request(app) #this function is responsible of introducing the base url and the api key defined in requests.py

    return app

