#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from .base import db
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/articledb'
# db = SQLAlchemy(app)


# import datetime

tag_article = db.Table('tag_article',
    db.Column('tags_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('articles_id', db.Integer, db.ForeignKey('articles.id'))
)

class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    tag_article = db.relationship('Articles', secondary=tag_article,
                                  backref=db.backref('tags',
                                                     lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tags %r>' % self.name

class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    publish = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text,nullable=False)
    user = db.Column(db.String, nullable=False)
    category = db.Column(db.String,nullable=False)
    copy = db.Column(db.Boolean,nullable=False,default=False)
    '''多个标签对多篇文章'''
    tag_article = db.relationship('Tags', secondary=tag_article,
                                  backref=db.backref('articles',
                                                     lazy='dynamic'))

    def __init__(self,
                 title, user,content,category):
        self.user = user
        self.title = title
        self.content = content
        self.category = category

    def __repr__(self):
        return "<Articles %r>" % self.title

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    user = db.Column(db.String, nullable=False)
    publish = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text,nullable=False)
    articles_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    article = db.relationship('Articles', backref=db.backref('comments',
                                                              lazy='dynamic'))

    def __init__(self,user, content):
        self.user = user
        self.content = content

    def __repr__(self):
        return "<Comments %r>" % self.content

class Replies(db.Model):
    __tablename__ = 'replies'
    id = db.Column(db.Integer,primary_key=True)
    user = db.Column(db.String, nullable=False)
    publish = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text,nullable=False)
    comments_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    comment = db.relationship('Comments', backref=db.backref('replies',
                                                              lazy='dynamic'))

    def __init__(self, user,content):
        self.user = user
        self.content = content

    def __repr__(self):
        return "<Replies %r>" % self.content

