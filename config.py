import os

class Config:
    '''
    General configuration parent class
    '''
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # It is not advisable to store files inside the database. Instead we store the files inside our application and we store the path to the files in our database.

    # #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'                  #Flask uses the Flask-Mail extension to send emails to users.
    MAIL_PORT = 587
    MAIL_USE_TLS = True                                  #enables a transport layer security to secure the emails when sending the emails.
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config): 
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugambi254:pitchdb@localhost/watchlist_test'          # Here we create a new database watchlist_test. We use WITH TEMPLATE to copy the schema of the watchlist database so both databases can be identical. ie CREATE DATABASE watchlist_test WITH TEMPLATE watchlist


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugambi254:pitchdb@localhost/watchlist'     #this is the location of the database with authentication.
    DEBUG = True
    #enables debig mode in our app

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}