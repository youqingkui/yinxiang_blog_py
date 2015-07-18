#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from config import config

db = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # 附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
