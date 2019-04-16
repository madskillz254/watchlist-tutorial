from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

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

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

        # setting config
    from .requests import configure_request
    configure_request(app) #this function is responsible of introducing the base url and the api key defined in requests.py

    return app

