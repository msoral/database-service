from flask import Flask
import connexion

from app.utils import get_config

_API = "/database_service"
_VERSION = "/v1"


def create_app(config_name=None):
    """
    Entry point to the Flask RESTful Server application.
    """
    config = get_config(config_name)
    # Create and configure the app
    # conn_app = connexion.App(__name__, specification_dir=f"{config.PROJECT_ROOT}/swagger")
    # app = conn_app.app
    # conn_app.add_api("swagger.yaml")
    app = Flask(__name__, instance_relative_config=True)
    try:

        app.config.from_object(config)
    except ImportError:
        raise Exception('Invalid Config')

    with app.app_context():
        # Import resources, blueprints if there is a database initialize here.
        from .endpoints import bp_temp

        # Register Blueprints
        app.register_blueprint(bp_temp, url_prefix=f"{_API}{_VERSION}/temp")

        return app
