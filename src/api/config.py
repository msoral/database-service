from dataclasses import dataclass
from typing import Optional


@dataclass()
class FlaskConfig:
    SQLALCHEMY_DATABASE_URI: str
    ENV: str = "development"
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
