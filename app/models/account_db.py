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


ROLES = [ ('admin', 'admin'),
         ('editor', 'editor'),
         ('writer', 'writer'),
         ('visitor', 'visitor') ]
class User(db.Model,UserMixin):
    __bind_key__ = 'blog'
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    passwd = db.Column(db.String,nullable=False)
    roles = db.Column(db.String,nullable=False)
    is_superuser = db.Column(db.Boolean,default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    registered_time = db.Column(db.DateTime, nullable=False)
    confirmed_time = db.Column(db.DateTime, nullable=True)
    introduce = db.Column(db.Text,nullable=True)
    school = db.Column(db.String,nullable=True)

    def __init__(self, name,email, passwd,
                 roles,
                 registered_time = datetime.datetime.now(),
                 confirmed_time=None,
                 introduce = None,
                 school = None):
        self.name = name
        self.email = email
        self.passwd = self.set_password(passwd)
        self.registered_time = registered_time
        self.confirmed_time = confirmed_time
        self.roles = roles
        self.school = school
        self.introduce = introduce

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return "<User %r>" % self.name


# from flask import Flask
# from flask.ext.login import UserMixin
# from flask.ext.sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, \
     # check_password_hash
# import datetime

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/articledb'
# db = SQLAlchemy(app)


# ROLES = [ ('admin', 'admin'),
         # ('editor', 'editor'),
         # ('writer', 'writer'),
         # ('visitor', 'visitor') ]
# class User(db.Model,UserMixin):
    # __tablename__ = 'users'
    # id = db.Column(db.Integer, primary_key=True,)
    # name = db.Column(db.String, unique=True)
    # email = db.Column(db.String, unique=True)
    # passwd = db.Column(db.String,nullable=False)
    # roles = db.Column(db.String,default='visitor')
    # is_superuser = db.Column(db.Boolean,default=False)
    # is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    # registered_time = db.Column(db.DateTime, nullable=False)
    # confirmed_time = db.Column(db.DateTime, nullable=True)

    # def __init__(self, name,email, passwd,
                 # is_superuser,is_confirmed,
                 # roles,
                 # registered_time = datetime.datetime.now(),
                 # confirmed_time=None):
        # self.name = name
        # self.email = email
        # self.passwd = self.set_password(passwd)
        # self.is_superuser = is_superuser
        # self.is_confirmed = is_confirmed
        # self.registered_time = registered_time
        # self.confirmed_time = confirmed_time
        # self.roles = roles.choices(ROLES)

    # def set_password(self, password):
        # self.pw_hash = generate_password_hash(password)
        # return self.pw_hash

    # def check_password(self, password):
        # return check_password_hash(self.pw_hash, password)
    # # def is_authenticated(self):
        # # return True

    # # def is_active(self):
        # # return True

    # # def is_anonymous(self):
        # # return False

    # # def get_id(self):
        # # return unicode(self.id)

    # def __repr__(self):
        # return "<User %r>" % self.name
