#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: articledb.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-29 02:07:53
# *************************************************************************
from maple.extensions import db
from datetime import datetime
from flask_maple.models import ModelMixin


class Question(db.Model, ModelMixin):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(48), nullable=False)
    describ = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    is_private = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    author_id = db.Column(
        db.Integer, db.ForeignKey(
            'users.id', ondelete="CASCADE"))
    author = db.relationship(
        'User',
        backref=db.backref(
            'questions', cascade='all,delete-orphan', lazy='dynamic'))

    __mapper_args__ = {"order_by": created_at.desc()}

    def __repr__(self):
        return "<Question %r>" % self.title

    def __str__(self):
        return self.title
