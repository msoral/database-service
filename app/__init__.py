from flask import Flask


def create_app(config_filename):
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    with app.app_context():
        # Include the resources
        from . import endpoints

        # Register Blueprints

