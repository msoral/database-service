import os


class BaseConfig:
    DEBUG = False
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    DOMAIN = 'http://localhost:5000'


class TestingConfig(BaseConfig):
    ENV = 'testing'
    TESTING = True
    DOMAIN = 'http://testserver'

    # Use memory for DB files
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

