# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

development = True


class Config(object):
    DEBUG = True
    TESTING = False
    BOOTSTRAP_FONTAWESOME = True
    SECRET_KEY = ""
    CSRF_ENABLED = True

    RECAPTCHA_PUBLIC_KEY = ""
    RECAPTCHA_PRIVATE_KEY = ""

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'emailid@gmail.com'
    MAIL_PASSWORD = 'googlepassword'  

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://userid:password@localhost/dbname'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://userid:password@localhost/dbname'


class TestingConfig(Config):
    TESTING = True
