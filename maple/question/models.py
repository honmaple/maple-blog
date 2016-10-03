#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: articledb.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-29 02:07:53
# *************************************************************************
from maple import db
from datetime import datetime


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(48), nullable=False)
    describ = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    is_private = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship(
        'User', backref=db.backref(
            'questions', lazy='dynamic'))

    __mapper_args__ = {"order_by": created_at.desc()}

    def __repr__(self):
        return "<Question %r>" % self.title

    @classmethod
    def get(cls, queId):
        return cls.query.filter_by(id=queId).first_or_404()

    @classmethod
    def get_question_list(cls, page=1, filter_dict=dict()):
        if not filter_dict:
            return cls.query.paginate(page, 18, True)
        return cls.query.filter_by(**filter_dict).paginate(page, 18, True)
