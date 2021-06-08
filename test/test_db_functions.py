import pytest
from sqlalchemy import create_engine
from database_service import config


@pytest.fixture(scope="session")
def connection():
    engine = create_engine(
        config.settings.SQLALCHEMY_DATABASE_URI
    )
    return engine.connect()


@pytest.fixture(scope="session")
def setup_database(connection):
    models.Base.metadata.bind = connection
    models.Base.metadata.create_all()

    seed_database()

    yield

    models.Base.metadata.drop_all()

