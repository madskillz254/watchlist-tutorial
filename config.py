import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugambi254:pitchdb@localhost/watchlist'   #this is the location of the database with authentication.
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # It is not advisable to store files inside the database. Instead we store the files inside our application and we store the path to the files in our database.

    # #  email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'                  #Flask uses the Flask-Mail extension to send emails to users.
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True                                  #enables a transport layer security to secure the emails when sending the emails.
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config): 
    '''
    Production  configuration child class
    this is a subclass ie all functions and methods declared in the parent class ie config will be extended or also made available to this class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    #enables debig mode in our app

config_options = {
'development':DevConfig,
'production':ProdConfig
}
