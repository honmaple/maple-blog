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
import datetime


class Category(db.Model):
    __bind_key__ = 'category'
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    article = db.relationship('Articles',backref='category',lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class Tags(db.Model):
    __bind_key__ = 'tags'
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    article = db.relationship('Articles',backref='tags',lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tags %r>' % self.name

class Articles(db.Model):
    __bind_key__ = 'articles'
    __tablename__ = 'articles'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    publish = db.Column(db.DateTime, nullable=False)
    summary = db.Column(db.Text,nullable=False)
    content = db.Column(db.Text,nullable=False)
    user = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    tags_id = db.Column(db.Integer, db.ForeignKey('tags.id'))

    def __init__(self, 
                 title, user,
                 summary,content,
                 category_id,tags_id,
                 publish = datetime.datetime.now().strftime('%F %X')):

        self.title = title
        self.publish = publish
        self.summary = summary
        self.content = content
        self.user = user
        self.category_id = category_id
        self.tags_id = tags_id

    def __repr__(self):
        return "<Articles %r>" % self.title

# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/articledb'
# db = SQLAlchemy(app)


# import datetime

# class Category(db.Model):
    # __tablename__ = 'category'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50))
    # article = db.relationship('Articles',backref='category',lazy='dynamic')

    # def __init__(self, name):
        # self.name = name

    # def __repr__(self):
        # return '<Category %r>' % self.name

# class Tags(db.Model):
    # __tablename__ = 'tags'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50))
    # article = db.relationship('Articles',backref='tags',lazy='dynamic')

    # def __init__(self, name):
        # self.name = name

    # def __repr__(self):
        # return '<Tags %r>' % self.name

# class Articles(db.Model):
    # __tablename__ = 'articles'
    # id = db.Column(db.Integer,primary_key=True)
    # title = db.Column(db.String(50), nullable=False)
    # publish = db.Column(db.DateTime, nullable=False)
    # summary = db.Column(db.Text,nullable=False)
    # content = db.Column(db.Text,nullable=False)
    # user = db.Column(db.String, nullable=False)
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # tags_id = db.Column(db.Integer, db.ForeignKey('tags.id'))

    # def __init__(self, 
                 # title, user,
                 # summary,content,
                 # category_id,tags_id,
                 # publish = datetime.datetime.now().strftime('%F %X')):

        # self.title = title
        # self.publish = publish
        # self.summary = summary
        # self.content = content
        # self.user = user
        # self.category_id = category_id
        # self.tags_id = tags_id

    # def __repr__(self):
        # return "<Articles %r>" % self.title
