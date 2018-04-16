#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: models.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-24 15:13:33 (CST)
# Last Update: 星期一 2018-02-05 13:34:41 (CST)
#          By:
# Description:
# **************************************************************************
from maple.extensions import db
from datetime import datetime
from maple.extensions import db
from maple.common.models import BaseModel
from flask_login import UserMixin
from werkzeug.security import (generate_password_hash, check_password_hash)
from datetime import datetime
from itsdangerous import (URLSafeTimedSerializer, BadSignature,
                          SignatureExpired)
from flask import current_app
from flask_maple.auth.models import UserMixin


class Notice(db.Model):
    __tablename__ = 'notices'
    id = db.Column(db.Integer, primary_key=True)
    notice = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)

    __mapper_args__ = {"order_by": created_at.desc()}

    def __repr__(self):
        return "<Notice %r>" % self.id


class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    path = db.Column(db.String(128), nullable=False, unique=True)
    url = db.Column(db.String(360), unique=True)

    def __repr__(self):
        return "<Images %r>" % self.name

    def __str__(self):
        return self.name


ROLES = [('admin', 'admin'), ('editor', 'editor'), ('writer', 'writer'),
         ('visitor', 'visitor')]


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    roles = db.Column(db.String, nullable=False)
    confirmed_time = db.Column(db.DateTime, nullable=True)
    send_email_time = db.Column(db.DateTime, nullable=True)
    introduce = db.Column(db.Text, nullable=True)
    school = db.Column(db.String, nullable=True)

    def update_password(self, password):
        self.password = generate_password_hash(password)
        db.session.commit()

    def update_infor(self, form):
        self.school = form.school.data
        self.introduce = form.introduce.data
        db.session.commit()

    @property
    def is_logined(self):
        return self.is_authenticated

    @property
    def token(self):
        config = current_app.config
        secret_key = config.setdefault('SECRET_KEY')
        salt = config.setdefault('SECRET_KEY_SALT')
        serializer = URLSafeTimedSerializer(secret_key)
        token = serializer.dumps(self.username, salt=salt)
        return token

    @staticmethod
    def check_token(token, max_age=86400):
        config = current_app.config
        secret_key = config.setdefault('SECRET_KEY')
        salt = config.setdefault('SECRET_KEY_SALT')
        serializer = URLSafeTimedSerializer(secret_key)
        try:
            username = serializer.loads(token, salt=salt, max_age=max_age)
        except BadSignature:
            return False
        except SignatureExpired:
            return False
        user = User.query.filter_by(username=username).first()
        if user is None:
            return False
        return user
