# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.mongoengine import MongoEngine

from flask_musers import login_manager

from config.blueprints import register_blueprints


db = MongoEngine()


def create_app(configuration='Production'):
    settings = 'config.settings.%s' % configuration

    app = Flask(__name__)
    app.config.from_object(settings)

    db.init_app(app)
    login_manager.init_app(app)

    register_blueprints(app)

    return app
