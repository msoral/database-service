import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
import yaml
import dacite
from src.api.config import FlaskConfig

PROJECT_ROOT = Path(__file__).parent.parent


@dataclass()
class Config:
    # Default values are for local development.
    # Please provide a config.yaml file for production.
    Flask: FlaskConfig

    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "123123"
    dialect: str = "postgresql"
    driver: str = "psycopg2"
    db: Optional[str] = "algotrading"


def set_config_from_file(config_file):
    if Path.is_file(Path(config_file)):
        with open(config_file, "r") as yaml_file:
            raw_yaml = yaml.safe_load(yaml_file)
            return dacite.from_dict(Config, raw_yaml)
    else:
        raise FileNotFoundError(config_file)
