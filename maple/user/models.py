#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
# *************************************************************************
from maple import db, cache
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, \
     check_password_hash

ROLES = [('admin', 'admin'), ('editor', 'editor'), ('writer', 'writer'),
         ('visitor', 'visitor')]


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    passwd = db.Column(db.String, nullable=False)
    roles = db.Column(db.String, nullable=False)
    is_superuser = db.Column(db.Boolean, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    registered_time = db.Column(db.DateTime, nullable=False)
    confirmed_time = db.Column(db.DateTime, nullable=True)
    send_email_time = db.Column(db.DateTime, nullable=True)
    introduce = db.Column(db.Text, nullable=True)
    school = db.Column(db.String, nullable=True)

    def __init__(self,
                 name,
                 email,
                 passwd,
                 roles,
                 confirmed_time=None,
                 introduce=None,
                 school=None):
        self.name = name
        self.email = email
        self.passwd = self.set_password(passwd)
        self.confirmed_time = confirmed_time
        self.roles = roles
        self.school = school
        self.introduce = introduce

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    # def check_password(self, password):
    #     return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return "<User %r>" % self.name

    @staticmethod
    def load_by_name(name):
        user = User.query.filter_by(name=name).first()
        return user

    @staticmethod
    def load_by_email(email):
        user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def check_password(user_password, password):
        return check_password_hash(user_password, password)
