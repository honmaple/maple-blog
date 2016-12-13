#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: models.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-13 14:42:26 (CST)
# Last Update:星期二 2016-12-13 14:47:12 (CST)
#          By:
# Description:
# **************************************************************************
from maple.extensions import db
from flask_maple.models import ModelMixin
from datetime import datetime
from maple.user.models import User


class TimeLine(db.Model, ModelMixin):
    __tablename__ = 'timeline'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    hide = db.Column(db.Boolean, nullable=True, default=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    author_id = db.Column(
        db.Integer, db.ForeignKey(
            'users.id', ondelete="CASCADE"))
    author = db.relationship(
        User,
        backref=db.backref(
            'timelines', cascade='all,delete-orphan', lazy='dynamic'))

    def __repr__(self):
        return "<TimeLine %r>" % self.content[:10]

    def __str__(self):
        return self.content[:10]
