# -*- coding:utf-8 -*-
import os
import json

from flask import Flask, jsonify
from flask import request
from flask_session import Session

# from flask_babel import Babel
# from flask_babel import gettext as _

from app.exts import db
from app.namespace import blueprint
from config import config
# from app.exts import init_ext


def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.config.from_object(config[config_name])
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    config[config_name].init_app(app)
    # celery.conf.update(app.config)
    # Session(app)
    # init_ext(app)

    @app.route('/')
    def index():
        data = {
            'status': 1,
            'msg': 'success',
            'data': 'index'
        }
        return jsonify(data)

    app.register_blueprint(blueprint, url_prefix='')

    return app
