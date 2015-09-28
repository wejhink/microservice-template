# -*- coding: utf-8 -*-
from flask import Flask

from .api import api_bp
from .settings import BaseConfig


def create_app(config=None, config_obj=None):
    """Flask app factory function."""
    app = Flask(__name__)
    configure_app(app, config=config, config_obj=config_obj)
    app.register_blueprint(api_bp)
    return app


def configure_app(app, config=None, config_obj=None):
    """Configure application instance."""
    app.config.from_object(config_obj or BaseConfig)
    if config is not None:
        app.config.from_pyfile(config)
