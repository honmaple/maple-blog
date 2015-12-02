#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: articledb.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-29 02:07:53
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from .base import db
import datetime

tags = db.Table('tags',
                db.Column('comment_id',db.Integer,
                          db.ForeignKey('comment.id')),
                db.Column('reply_id',db.Integer,
                          db.ForeignKey('reply.id'))
                )

class Commentdb(db.Model):
    # __bind_key__ = 'comments'
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    # comment_name = db.Column(db.String, nullable=False)
    comment_user = db.relationship('Replydb',
                                   secondary=tags,
                                   backref=db.backref('pages', lazy='dynamic'))
    # comment = db.Column(db.Text,nullable=False)
    comment = db.relationship('Replydb', backref='reply',
                                lazy='dynamic')
    comment_publish = db.Column(db.DateTime, nullable=False)

    def __init__(self, comment_name,comment, comment_publish = datetime.datetime.now()):
        self.comment_name = comment_name
        self.comment = comment
        self.comment_publish = comment_publish

    def __repr__(self):
        return "<Commentdb %r>" % self.comment

class Replydb(db.Model):
    __tablename__ = 'replays'
    id = db.Column(db.Integer,primary_key=True)
    reply_user = db.Column(db.String, nullable=False)
    reply_id = db.Column(db.Text,nullable=False)
    reply_publish = db.Column(db.DateTime, nullable=False)

# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/commentdb'
# db = SQLAlchemy(app)


# import datetime

# class Commentdb(db.Model):
# __tablename__ = 'comments'
# id = db.Column(db.Integer,primary_key=True)
# name = db.Column(db.String, nullable=False)
# comment = db.Column(db.Text,nullable=False)
# publish = db.Column(db.DateTime, nullable=False)

    # def __init__(self, name,comment, publish = datetime.datetime.now()):
    # self.name = name
    # self.comment = comment
    # self.publish = publish

    # def __repr__(self):
    # return "<Commentdb %r>" % self.comment
