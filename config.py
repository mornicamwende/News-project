import os


class Config:
    '''
    General configuration parent class
    '''
    # MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class
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

config_options = {
'development': DevConfig,
'production': ProdConfig
}