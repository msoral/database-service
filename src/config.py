from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import dacite
import yaml

PROJECT_ROOT = Path(__file__).parent.parent

"""
I believe it might be more clear to other users to take these configuration parameters separately. However, due to time
concerns, I will leave this section commented out, so I can return to it later to implement it later. If the project's
complexity increases I might consider separating the configuration to multiple objects. 
"""
# @dataclass()
# class DatabaseConfig:
#     user: str = "postgres"
#     password: str = "123123"
#     url: str = "localhost"
#     port: int = 5432
#     database: str = "algotrader"
#
#     @property
#     def DATABASE_URI(self):
#         return f"postgresql+psycopg2://{self.user}:{self.password}@{self.url}:{self.port}/{self.database}"


@dataclass()
class Config:
    # Default values are for local development.
    # Please provide a config.yaml file for production.
    FLASK_ENV: str
    DEBUG: bool
    SQLALCHEMY_TRACK_MODIFICATIONS: bool
    SQLALCHEMY_DATABASE_URI: str


class DefaultConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    FLASK_ENV = "dev"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def load_config_from_yaml(config_file):
    if Path.is_file(Path(config_file)):
        with open(config_file, "r") as yaml_file:
            raw_yaml = yaml.safe_load(yaml_file)
            return dacite.from_dict(Config, raw_yaml)
    else:
        raise FileNotFoundError(config_file)
