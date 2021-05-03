import connexion
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from src.api import encoder
from src.config import PROJECT_ROOT, DefaultConfig, load_config_from_yaml

db = SQLAlchemy()
migrate = Migrate()
api = Api


def create_app(config_file=None):
    """
    Entry point to the Flask RESTful Server application.
    """
    # Create a connexion app with the open
    conn_app = connexion.App(__name__, specification_dir=f"{PROJECT_ROOT}/openapi")
    # This creates a FlaskApp that we can use with other flask-* libraries.
    app = conn_app.app
    app.json_encoder = encoder.JSONEncoder
    conn_app.add_api(
        "openapi.yaml", arguments={"title": "Database Service"}, pythonic_params=True
    )
    print(f"!!!Config File: {config_file}!!!")
    if config_file is None:
        print(
            "Did not specify a config.yaml file, starting the app with default configuration."
        )
        app.config.from_object(DefaultConfig)
    else:
        cfg = load_config_from_yaml(config_file)
        print(f"Starting the app with the following configuration: {cfg}")
        app.config.from_object(cfg)
    print("===================================================")
    print(app.config)
    print("===================================================")

    # Initialize flask libraries
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        print("Inside app context!")
        db.create_all()
        # We must return connexion to benefit from the openapi specification UI.
        return conn_app
