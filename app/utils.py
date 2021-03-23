import os
from werkzeug.utils import import_string

from config import BaseConfig

CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
}


def get_config(config_name=None) -> BaseConfig:
    flask_config_name = os.getenv('FLASK_CONFIG', 'development')
    if config_name is not None:
        flask_config_name = config_name
    return import_string(CONFIG_NAME_MAPPER[flask_config_name])