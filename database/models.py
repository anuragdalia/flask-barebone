# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
from enum import Enum

from flask_login._compat import unicode

from main import db


class Roles(Enum):
    ANY = 1
    ADMIN = 2
    CAMPAIGNER = 3
    SELLER = 4


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    dob = db.Column(db.Date())
    email = db.Column(db.VARCHAR(50), unique=True)
    password = db.Column(db.VARCHAR(50))
    phone = db.Column(db.VARCHAR(15), unique=True)
    urole = db.Column(db.Enum(Roles), default=Roles.BOTOWNER)
    activated = db.Column(db.Boolean(False))

    def __init__(self, name, dob, email, password, phone, urole):
        self.name = name
        self.dob = dob
        self.email = email
        self.password = password
        self.phone = phone
        self.activated = False
        self.urole = urole

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def get_urole(self):
        return self.urole

    def __repr__(self):
        return '<User %r>' % (self.name)

    def activate(self):
        self.activated = True
        db.session.add(self)
        db.session.commit()
