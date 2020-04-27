import os 

class Config:
    SOURCE_NEWS_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey={}'
    CATEGORIZED_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}