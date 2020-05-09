# -*- coding: utf-8 -*-
# import redis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from celery import Celery, platforms

from config import BaseConfig
from config import REDISBASES

db = SQLAlchemy()
migrate = Migrate()

# from app import models


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app=app, db=db)


# def auto_rollback(func):
#     def make(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             db.session.rollback()
#             raise Exception(repr(e))
#
#     return make

#
# platforms.C_FORCE_ROOT = True
# celery = Celery(__name__, broker=BaseConfig.CELERY_BROKER_URL, backend=BaseConfig.CELERY_RESULT_BACKEND)
#
# pool = redis.ConnectionPool(host=REDISBASES['HOST'], port=REDISBASES['PORT'], password=REDISBASES['PWD'],
#                             decode_responses=True)
