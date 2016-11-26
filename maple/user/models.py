#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
# *************************************************************************
from maple.extensions import db
from maple.common.models import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, \
     check_password_hash
from datetime import datetime
from flask_maple.permission.models import Group

ROLES = [('admin', 'admin'), ('editor', 'editor'), ('writer', 'writer'),
         ('visitor', 'visitor')]

group_user = db.Table(
    'group_user',
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')))


class User(db.Model, UserMixin, BaseModel):
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
    groups = db.relationship(
        Group, secondary=group_user, backref=db.backref('users'))

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
