from dataclasses import dataclass
from typing import Optional


@dataclass()
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    dialect: str
    driver: str
    db: Optional[str] = "algotrading"

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @classmethod
    def uri(cls) -> str:
        # Creates the URI for the app to connect to the database
        return f"{cls.dialect}+{cls.driver}://{cls.user}:{cls.password}@{cls.host}:{cls.port}/{cls.db}"
