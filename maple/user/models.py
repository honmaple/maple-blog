#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
# *************************************************************************
from maple import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, \
     check_password_hash
from datetime import datetime

ROLES = [('admin', 'admin'), ('editor', 'editor'), ('writer', 'writer'),
         ('visitor', 'visitor')]


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    roles = db.Column(db.String, nullable=False)
    is_superuser = db.Column(db.Boolean, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    registered_time = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    confirmed_time = db.Column(db.DateTime, nullable=True)
    send_email_time = db.Column(db.DateTime, nullable=True)
    introduce = db.Column(db.Text, nullable=True)
    school = db.Column(db.String, nullable=True)

    # def __init__(self,
    #              username,
    #              email,
    #              password,
    #              roles,
    #              confirmed_time=None,
    #              introduce=None,
    #              school=None):
    #     self.username = username
    #     self.email = email
    #     self.password = self.set_password(password)
    #     self.confirmed_time = confirmed_time
    #     self.roles = roles
    #     self.school = school
    #     self.introduce = introduce

    def update_password(self, password):
        self.password = generate_password_hash(password)
        db.session.commit()

    def update_infor(self, form):
        self.school = form.school.data
        self.introduce = form.introduce.data
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User %r>" % self.username

    def __str__(self):
        return self.username

    @staticmethod
    def set_password(password):
        passwd_hash = generate_password_hash(password)
        return passwd_hash

    @staticmethod
    def load_by_name(name):
        user = User.query.filter_by(username=name).first()
        return user

    @staticmethod
    def load_by_email(email):
        user = User.query.filter_by(email=email).first()
        return user

    # @staticmethod
    # def check_password(user_password, password):
    #     return check_password_hash(user_password, password)
