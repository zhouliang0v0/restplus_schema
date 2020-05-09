# -*- coding:utf-8 -*-
import json
import re

from flask_migrate import MigrateCommand
from flask_script import Manager, Server

# from app.exts import db
from app import create_app
from flask import g, request, current_app
import os

# from app.ops.records.controls.request import Request
# from tools import generate_uuid

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    host='127.0.0.1', port='5000', threaded=True))


@app.before_request
def before_request():
    base_url = request.base_url
    g.method = request.method
    g.endpoint = request.endpoint
    g.error_code = 400
    g.ip = request.remote_addr
    g.url = g.method + '/' + base_url
    g.username = 'anonymous'
    g.uid = None
    g.token = None
    g.resource_id = ""
    g.event = None
    # g.request_id = generate_uuid.get_uuid()
    g.is_admin = False
    g.is_super_admin = False
    g.Roles = []
    g.get_params = {}

#
# @app.after_request
# def after_request(res):
#     try:
#         swagger = re.compile('swagger').findall(g.url)
#         docs = re.compile('docs').findall(g.url)
#         if not (swagger or docs):
#             Request.create(res)
#     except Exception as e:
#         db.session.rollback()
#         current_app.logger.error(e)
#     return res


if __name__ == '__main__':
    manager.run()
