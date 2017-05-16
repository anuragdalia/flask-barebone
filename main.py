# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from configuration import development as devmode

development = devmode

app = Flask(__name__, template_folder='./templates')

if not development:
    app.config.from_object('configuration.ProductionConfig')
else:
    app.config.from_object('configuration.DevelopmentConfig')

bs = Bootstrap(app)
db = SQLAlchemy(app)

migr = Migrate(app, db)

lm = LoginManager(app)
lm.login_view = "signin"
limiter = Limiter(app, key_func=get_remote_address, global_limits=["2000 per day", "500 per hour"])

csrf = CSRFProtect(app)
mail = Mail(app)

if __name__ == '__main__':
    app.run()
