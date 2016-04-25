#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: articledb.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-29 02:07:53
# *************************************************************************
from maple import db,cache
from flask_login import current_user


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(48), nullable=False)
    describ = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    private = db.Column(db.Boolean, nullable=False, default=False)
    private_id = db.Column(db.Integer, nullable=True)
    publish = db.Column(db.DateTime, nullable=False)

    __mapper_args__ = {"order_by": publish.desc()}

    # def __init__(self, author, title, describ, answer):
    #     self.author = author
    #     self.title = title
    #     self.describ = describ
    #     self.answer = answer

    def __repr__(self):
        return "<Questions %r>" % self.title

    @staticmethod
    @cache.cached(timeout=60, key_prefix='questions:id')
    def load_by_id(qid):
        return Questions.query.filter_by(id=qid).first_or_404()

    @staticmethod
    @cache.cached(timeout=60, key_prefix='questions:id')
    def load_by_author(name):
        return Questions.query.filter_by(author=name).all()

    @staticmethod
    @cache.cached(timeout=60, key_prefix='questions:id')
    def load_by_private():
        questions = Questions.query.filter_by(author=current_user.name,
                                              private=True).all()
        return questions
