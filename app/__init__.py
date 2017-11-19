import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask("transport-crud")
    app.config.from_object(os.environ["APP_SETTINGS"])
    db.init_app(app)

    mapping_database()
    registry_blueprints(app)
    return app


def registry_blueprints(app):
    from .mod_transport.api import mod_transport

    # REGISTERING BLUEPRINTS
    app.register_blueprint(mod_transport)


def mapping_database():
    from .mod_transport.transport_model import Transport





