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


tag_article = db.Table('tag_article',
    db.Column('tags_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('articles_id', db.Integer, db.ForeignKey('articles.id'))
)

class Category(db.Model):
    __bind_key__ = 'articles'
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class Tags(db.Model):
    __bind_key__ = 'articles'
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
    __bind_key__ = 'articles'
    __tablename__ = 'articles'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    publish = db.Column(db.DateTime, nullable=False)
    summary = db.Column(db.Text,nullable=False)
    content = db.Column(db.Text,nullable=False)
    user = db.Column(db.String, nullable=False)
    '''一个分类对多篇文章'''
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('articles',
                                                              lazy='dynamic'))
    '''多个标签对多篇文章'''
    tag_article = db.relationship('Tags', secondary=tag_article,
                                  backref=db.backref('articles',
                                                     lazy='dynamic'))

    def __init__(self, 
                 title, user,
                 summary,content,
                 publish = datetime.datetime.now().strftime('%F %X')):

        self.title = title
        self.publish = publish
        self.summary = summary
        self.content = content
        self.user = user

    def __repr__(self):
        return "<Articles %r>" % self.title

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/articledb'
# db = SQLAlchemy(app)


# import datetime

# tag_article = db.Table('tag_article',
    # db.Column('tags_id', db.Integer, db.ForeignKey('tags.id')),
    # db.Column('articles_id', db.Integer, db.ForeignKey('articles.id'))
# )

# class Category(db.Model):
    # __tablename__ = 'category'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50))

    # def __init__(self, name):
        # self.name = name

    # def __repr__(self):
        # return '<Category %r>' % self.name

# class Tags(db.Model):
    # __tablename__ = 'tags'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50))

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
    # '''一个分类对多篇文章'''
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # category = db.relationship('Category', backref=db.backref('articles',
                                                              # lazy='dynamic'))
    # '''多个标签对多篇文章'''
    # tag_article = db.relationship('Tags', secondary=tag_article,
                                  # backref=db.backref('articles',
                                                     # lazy='dynamic'))

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
