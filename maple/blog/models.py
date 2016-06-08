#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
# *************************************************************************
from maple import db
from datetime import datetime

tag_article = db.Table('tag_article', db.Column('tags_id', db.Integer,
                                                db.ForeignKey('tags.id')),
                       db.Column('articles_id', db.Integer,
                                 db.ForeignKey('articles.id')))


class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # def __init__(self, name):
    #     self.name = name

    def __repr__(self):
        return '<Tags %r>' % self.name

    @staticmethod
    def load_by_name(name):
        return Tags.query.filter_by(name=name).first_or_404()


class Articles(db.Model):
    # query_class = ArticleQuery
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    publish = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.now())
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String, nullable=False)
    copy = db.Column(db.Boolean, nullable=True, default=False)
    # search_vector = db.Column(TSVectorType('title', 'content',
    #                                         weights={'title': 'A', 'content': 'B'}))
    '''多个标签对多篇文章'''
    tags = db.relationship(
        'Tags',
        secondary=tag_article,
        backref=db.backref('articles', lazy='dynamic'))

    __mapper_args__ = {"order_by": publish.desc()}

    # def __init__(self, title, author, content, category):
    #     self.author = author
    #     self.title = title
    #     self.content = content
    #     self.category = category

    def __repr__(self):
        return "<Articles %r>" % self.title

    @staticmethod
    def load_by_id(qid):
        return Articles.query.filter_by(id=qid).first_or_404()

    @staticmethod
    def load_by_tag(tag):
        article = Articles.query.join(Articles.tags).\
                  filter(Tags.name == tag).all()
        return article

    @staticmethod
    def load_by_category(category):
        return Articles.query.filter_by(category=category).all()


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=False)
    publish = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    articles_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    article = db.relationship(
        'Articles', backref=db.backref('comments', lazy='dynamic'))

    def __init__(self, author, content):
        self.author = author
        self.content = content

    def __repr__(self):
        return "<Comments %r>" % self.content

# class Replies(db.Model):
#     __tablename__ = 'replies'
#     id = db.Column(db.Integer, primary_key=True)
#     author = db.Column(db.String, nullable=False)
#     publish = db.Column(db.DateTime, nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     comments_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
#     comment = db.relationship('Comments',
#                               backref=db.backref('replies',
#                                                  lazy='dynamic'))

#     def __init__(self, author, content):
#         self.author = author
#         self.content = content

#     def __repr__(self):
#         return "<Replies %r>" % self.content
