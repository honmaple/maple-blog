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

class Comments(db.Model):
    __bind_key__ = 'comments'
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    page_title = db.Column(db.String, nullable=False)
    comment_user = db.Column(db.String, nullable=False)
    comment_publish = db.Column(db.DateTime, nullable=False)
    comment_content = db.Column(db.Text,nullable=False)
    reply = db.relationship('Replies',backref='comments',lazy='dynamic')

    def __init__(self, page_title,
                 comment_user,
                 comment_content,
                 comment_publish = datetime.datetime.now()):
        self.page_title = page_title
        self.comment_user = comment_user
        self.comment_content = comment_content
        self.comment_publish = comment_publish

    def __repr__(self):
        return "<Comments %r>" % self.comment_content

class Replies(db.Model):
    __bind_key__ = 'replies'
    __tablename__ = 'replies'
    id = db.Column(db.Integer,primary_key=True)
    reply_user = db.Column(db.String, nullable=False)
    reply_publish = db.Column(db.DateTime, nullable=False)
    reply_content = db.Column(db.Text,nullable=False)
    comments_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    def __init__(self, reply_user,reply_content,
                 reply_publish = datetime.datetime.now(),
                 comments_id = comments_id):
        self.reply_user = reply_user
        self.reply_content = reply_content
        self.reply_publish = reply_publish
        self.comments_id = comments_id

    def __repr__(self):
        return "<Replies %r>" % self.reply_content


# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/commentdb'
# db = SQLAlchemy(app)


# import datetime

# class Comments(db.Model):
    # __tablename__ = 'comments'
    # id = db.Column(db.Integer,primary_key=True)
    # page_title = db.Column(db.String, nullable=False)
    # comment_user = db.Column(db.String, nullable=False)
    # comment_publish = db.Column(db.DateTime, nullable=False)
    # comment_content = db.Column(db.Text,nullable=False)
    # reply = db.relationship('Replies',backref='comments',lazy='dynamic')

    # def __init__(self, page_title,
                 # comment_user,
                 # comment_content,
                 # comment_publish = datetime.datetime.now()):
        # self.page_title = page_title
        # self.comment_user = comment_user
        # self.comment_content = comment_content
        # self.comment_publish = comment_publish

    # def __repr__(self):
        # return "<Comments %r>" % self.comment_content

# class Replies(db.Model):
    # __tablename__ = 'replies'
    # id = db.Column(db.Integer,primary_key=True)
    # reply_user = db.Column(db.String, nullable=False)
    # reply_publish = db.Column(db.DateTime, nullable=False)
    # reply_content = db.Column(db.Text,nullable=False)
    # comments_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    # def __init__(self, reply_user,reply_content,
                 # reply_publish = datetime.datetime.now(),
                 # comments_id = comments_id):
        # self.reply_user = reply_user
        # self.reply_content = reply_content
        # self.reply_publish = reply_publish
        # self.comments_id = comments_id

    # def __repr__(self):
        # return "<Replies %r>" % self.reply_content
