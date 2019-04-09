class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    



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
