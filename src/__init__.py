import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config import PROJECT_ROOT

from .api.config import FlaskConfig
db = SQLAlchemy()
migrate = Migrate()


def create_app(cfg):
    """
    Entry point to the Flask RESTful Server application.
    """
    # Create and configure the app
    conn_app = connexion.App(__name__, specification_dir=f"{PROJECT_ROOT}/openapi")
    app = conn_app.app
    conn_app.add_api("openapi.yaml")
    app.config.from_object(cfg.Flask)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from src.database import __all__
        db.create_all()

        return conn_app
