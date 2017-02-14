#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
# *************************************************************************
from maple.extensions import db
from datetime import datetime
from flask_maple.models import ModelMixin

tag_blog = db.Table(
    'tag_blog', db.Column('tags_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('blogs_id', db.Integer, db.ForeignKey('blogs.id')))


class Tags(db.Model, ModelMixin):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    blogs = db.relationship(
        'Blog',
        secondary=tag_blog,
        backref=db.backref(
            'tags', lazy='dynamic'),
        lazy='dynamic')

    def __repr__(self):
        return '<Tags %r>' % self.name

    def __str__(self):
        return self.name


class Category(db.Model, ModelMixin):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

    def __str__(self):
        return self.name


class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'

    CONTENT_TYPE_MARKDOWN = '0'
    CONTENT_TYPE_ORGMODE = '1'

    CONTENT_TYPE = (('0', 'markdown'), ('1', 'org-mode'))

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    content_type = db.Column(
        db.String(10), nullable=False, default=CONTENT_TYPE_MARKDOWN)
    is_copy = db.Column(db.Boolean, nullable=True, default=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey(
            'categories.id', ondelete="CASCADE"))
    category = db.relationship(
        'Category',
        backref=db.backref(
            'blogs', cascade='all,delete-orphan', lazy='dynamic'))
    author_id = db.Column(
        db.Integer, db.ForeignKey(
            'users.id', ondelete="CASCADE"))
    author = db.relationship(
        'User',
        backref=db.backref(
            'blogs', cascade='all,delete-orphan', lazy='dynamic'))

    __mapper_args__ = {"order_by": created_at.desc()}

    def __repr__(self):
        return "<Blog %r>" % self.title

    def __str__(self):
        return self.title


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    content = db.Column(db.Text, nullable=False)
    blog_id = db.Column(
        db.Integer, db.ForeignKey(
            'blogs.id', ondelete="CASCADE"))
    blog = db.relationship(
        'Blog',
        backref=db.backref(
            'comments', cascade='all,delete-orphan', lazy='dynamic'))
    author_id = db.Column(
        db.Integer, db.ForeignKey(
            'users.id', ondelete="CASCADE"))
    author = db.relationship(
        'User',
        backref=db.backref(
            'comments', cascade='all,delete-orphan', lazy='dynamic'))

    def __repr__(self):
        return "<Comment %r>" % self.content
