# -*- coding:utf-8 -*-
import os
# import redis
from datetime import timedelta

# from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIL_TEMPLATE = os.path.join(BASE_DIR, 'templates', 'email')
UPLOAD_DIR = os.path.join(BASE_DIR, 'upload')  # 上传文件总路径

DATABASES = {
    'develop': {
        'MYSQL_HOST': '172.16.150.109',
        'MYSQL_POST': 3306,
        'MYSQL_DATABASE_NAME': 'rest_schema',
        'MYSQL_USER': 'zcl',
        'MYSQL_PWD': 'aaaaaa',
    },
    'testing': {
        'MYSQL_HOST': '127.0.0.1',
        'MYSQL_POST': 3306,
        'MYSQL_DATABASE_NAME': '',
        'MYSQL_USER': '',
        'MYSQL_PWD': '',
    },
    'product': {
        'MYSQL_HOST': '127.0.0.1',
        'MYSQL_POST': 3306,
        'MYSQL_DATABASE_NAME': 'rest_schema',
        'MYSQL_USER': 'zcl',
        'MYSQL_PWD': 'aaaaaa',
    },
}

REDISBASES = {
    'HOST': '172.16.150.109',
    'PORT': '6379',
    'PWD': '123456'
}


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    IS_CELERY = True

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_NATIVE_UNICODE = 'utf-8'
    SECURITY_PASSWORD_SALT = '421ebf5a-c882-a5fe-1d5d-b7ab7df2f8a2'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECRET_KEY = '421efbd1-e8a6-4117-2a23-d0ab14cc47ef'

    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = redis.Redis(host=REDISBASES['HOST'], port=REDISBASES['PORT'], password=REDISBASES['PWD'])
    # MONITOR_REDIS = redis.Redis(host=REDISBASES['HOST'], port=REDISBASES['PORT'], password=REDISBASES['PWD'], db=1)
    # COST_REDIS = redis.Redis(host=REDISBASES['HOST'], port=REDISBASES['PORT'], password=REDISBASES['PWD'], db=2)
    # TASK_ID_REDIS = redis.Redis(host=REDISBASES['HOST'], port=REDISBASES['PORT'], password=REDISBASES['PWD'], db=3)

    # SESSION_PERMANENT_SESSION_LIFETIME = 3600
    # SESSION_KEY_PREFIX = 'KStack_Enterprise'

    # CELERY_BROKER_URL = 'redis://:{}@{}:{}/4'.format(REDISBASES['PWD'], REDISBASES['HOST'], REDISBASES['PORT'])
    # CELERY_RESULT_BACKEND = 'redis://:{}@{}:{}/5'.format(REDISBASES['PWD'], REDISBASES['HOST'], REDISBASES['PORT'])

    # CELERY_ACCEPT_CONTENT = ['json', 'pickle']
    # CELERY_TASK_SERIALIZER = 'json'
    # CELERY_RESULT_SERIALIZER = 'json'
    # CELERYBEAT_SCHEDULE = {
    #     # 定义任务名称
    #     'TimingMonitor': {
    #         'task': 'TimingResourceMonitor',
    #         'schedule': timedelta(seconds=300),
    #         'options': {'queue': 'resource_monitor'}
    #     },
    #     'TimingCostCollect': {
    #         'task': 'TimingCostCollect',
    #         'schedule': crontab(hour='*/1', minute='0')
    #     },
    # }
    RESTPLUS_MASK_SWAGGER = False
    SQLALCHEMY_RECORD_QUERIES = True
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB
    IMAGE_UPLOAD_TIMEOUT = 10 * 60

    # 镜像文件上传超时时间

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(BaseConfig):
    DEBUG = True
    IS_CELERY = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'develop.db')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DATABASES['develop']['MYSQL_USER'],
                                                                                   DATABASES['develop']['MYSQL_PWD'],
                                                                                   DATABASES['develop']['MYSQL_HOST'],
                                                                                   DATABASES['develop']['MYSQL_POST'],
                                                                                   DATABASES['develop'][
                                                                                       'MYSQL_DATABASE_NAME'])


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DATABASES['testing']['MYSQL_USER'],
                                                                                   DATABASES['testing']['MYSQL_PWD'],
                                                                                   DATABASES['testing']['MYSQL_HOST'],
                                                                                   DATABASES['testing']['MYSQL_POST'],
                                                                                   DATABASES['testing'][
                                                                                       'MYSQL_DATABASE_NAME'])


class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DATABASES['testing']['MYSQL_USER'],
                                                                                   DATABASES['testing']['MYSQL_PWD'],
                                                                                   DATABASES['testing']['MYSQL_HOST'],
                                                                                   DATABASES['testing']['MYSQL_POST'],
                                                                                   DATABASES['testing'][
                                                                                       'MYSQL_DATABASE_NAME'])


config = {
    'develop': DevelopConfig,  # 开发环境
    'testing': TestingConfig,  # 测试环境
    'product': ProductConfig,  # 线上环境
    'default': DevelopConfig,  # 默认环境
}
