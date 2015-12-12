#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from .base import db
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, \
     check_password_hash
import datetime

class User(db.Model,UserMixin):
    __bind_key__ = 'users'
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    passwd = db.Column(db.String,nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, name,email, passwd,
                 registered_on = datetime.datetime.now(),
                 admin=False,
                 confirmed=False,
                 confirmed_on=None):
        self.name = name
        self.email = email
        self.passwd = self.set_password(passwd)
        self.registered_on = registered_on
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
    # def is_authenticated(self):
        # return True

    # def is_active(self):
        # return True

    # def is_anonymous(self):
        # return False

    # def get_id(self):
        # return unicode(self.id)

    def __repr__(self):
        return "<User %r>" % self.name


# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
# import datetime

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/Userdb'
# db = SQLAlchemy(app)


# class User(db.Model):
# __tablename__ = 'users'
# id = db.Column(db.Integer, primary_key=True)
# name = db.Column(db.String, unique=True)
# email = db.Column(db.String, unique=True)
# passwd = db.Column(db.String,nullable=False)
# registered_on = db.Column(db.DateTime, nullable=False)
# admin = db.Column(db.Boolean, nullable=False, default=False)
# confirmed = db.Column(db.Boolean, nullable=False, default=False)
# confirmed_on = db.Column(db.DateTime, nullable=True)

    # def __init__(self, name,email, passwd,
    # registered_on = datetime.datetime.now(),
    # admin=False,
    # confirmed=False,
    # confirmed_on=None):
    # self.name = name
    # self.email = email
    # self.passwd = passwd
    # self.registered_on = registered_on
    # self.admin = admin
    # self.confirmed = confirmed
    # self.confirmed_on = confirmed_on

    # def __repr__(self):
    # return "<User %r>" % self.name
