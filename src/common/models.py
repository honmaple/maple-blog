#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: models.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-26 14:56:23 (CST)
# Last Update:星期日 2017-2-12 16:34:41 (CST)
#          By:
# Description:
# **************************************************************************
from maple.extensions import db
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from flask_maple.models import ModelMixin


class CommonMixin(ModelMixin):
    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True)


class CommonTimeMixin(CommonMixin):
    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, default=datetime.utcnow())

    @declared_attr
    def updated_at(cls):
        return db.Column(
            db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


class CommonUserMixin(CommonTimeMixin):
    @declared_attr
    def user_id(cls):
        return db.Column(
            db.Integer, db.ForeignKey(
                'user.id', ondelete="CASCADE"))

    @declared_attr
    def user(cls):
        name = cls.__name__.lower()
        if not name.endswith('s'):
            name = name + 's'
        if hasattr(cls, 'user_related_name'):
            name = cls.user_related_name
        return db.relationship(
            'User',
            backref=db.backref(
                name, cascade='all,delete', lazy='dynamic'),
            uselist=False,
            lazy='joined')
