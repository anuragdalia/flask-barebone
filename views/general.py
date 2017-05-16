import json
import os
import random
import string
from functools import wraps

from flask import url_for, redirect, render_template, g, request, abort
from flask_login import current_user
from itsdangerous import URLSafeSerializer

import main
from webapp import app, lm, PAGES
from webapp.database.models import User, Bots, Roles
from flask import current_app


@app.route('/')
@app.route('/index/')
def index():
    if not current_user.is_authenticated:
        return render_template(PAGES['logged_out']["index"])
    else:
        if current_user.get_urole() in [Roles.BOTOWNER, Roles.ALL]:
            return render_template(PAGES['logged_in']["index"])
        else:
            return render_template('supervisor/landing.html')


# ====================
def get_activation_link(user):
    s = getsecret()
    payload = s.dumps(user.id)
    return url_for('activate_user', payload=payload, _external=True)


def redirect_dest(home):
    dest_url = request.args.get('next')
    if not dest_url:
        dest_url = url_for(home)
    return redirect(dest_url)


def getsecret(secret_key=None):
    if secret_key is None:
        secret_key = app.secret_key
    return URLSafeSerializer(secret_key)


def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


@app.before_request
def before_request():
    g.user = current_user


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@lm.user_loader
def load_user(uid):
    return User.query.get(int(uid))
