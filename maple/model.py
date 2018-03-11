#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: model.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-24 15:13:33 (CST)
# Last Update: Sunday 2018-03-11 21:43:48 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.auth.models import UserMixin, GroupMixin
from flask_maple.permission.models import PermissionMixin
from flask_maple.models import ModelUserMixin, ModelMixin

from flask import current_app
from itsdangerous import (URLSafeTimedSerializer, BadSignature,
                          SignatureExpired)
from flask_babel import format_datetime

from maple.extension import db
from maple.count import Count


class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    path = db.Column(db.String(128), nullable=False, unique=True)
    url = db.Column(db.String(360), unique=True)

    def __repr__(self):
        return "<Images %r>" % self.name

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    @staticmethod
    def _token_serializer():
        config = current_app.config
        secret_key = config.setdefault('SECRET_KEY')
        salt = config.setdefault('SECRET_KEY_SALT')
        serializer = URLSafeTimedSerializer(secret_key)
        return serializer, salt

    @property
    def token(self):
        serializer, salt = User._token_serializer()
        token = serializer.dumps(self.username, salt=salt)
        return token

    @staticmethod
    def check_token(token, max_age=86400):
        serializer, salt = User._token_serializer()
        try:
            username = serializer.loads(token, salt=salt, max_age=max_age)
        except BadSignature:
            return False
        except SignatureExpired:
            return False
        return User.query.filter_by(username=username).first()


class Group(db.Model, GroupMixin):
    __tablename__ = 'group'


class Permission(db.Model, PermissionMixin):
    __tablename__ = 'permission'


class TimeLine(db.Model, ModelUserMixin):
    __tablename__ = 'timeline'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    is_hidden = db.Column(db.Boolean, nullable=True, default=False)

    def __repr__(self):
        return "<TimeLine %r>" % self.content[:10]

    def __str__(self):
        return self.content[:10]

    @property
    def datetime_format(self):
        return format_datetime(self.created_at, 'Y-M-d H:M')

    def to_json(self):
        return {'id': self.id, 'content': self.content, 'hide': self.hide}


tag_blog = db.Table(
    'tag_blog', db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id')))


class Tag(db.Model, ModelMixin):
    __tablename__ = 'tag'
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
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

    def __str__(self):
        return self.name


class Blog(db.Model, ModelUserMixin):
    __tablename__ = 'blog'

    CONTENT_TYPE_MARKDOWN = '0'
    CONTENT_TYPE_ORGMODE = '1'

    CONTENT_TYPE = (('0', 'markdown'), ('1', 'org-mode'))

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_type = db.Column(
        db.String(10), nullable=False, default=CONTENT_TYPE_MARKDOWN)
    is_copy = db.Column(db.Boolean, nullable=True, default=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'category.id', ondelete="CASCADE"),
        nullable=False)
    category = db.relationship(
        'Category',
        backref=db.backref(
            'blogs', cascade='all,delete-orphan', lazy='dynamic'),
        uselist=False,
        lazy='joined')

    # __mapper_args__ = {"order_by": Blog.created_at.desc()}

    def __repr__(self):
        return "<Blog %r>" % self.title

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category.name,
            'tags': ','.join([tag.name for tag in self.tags]),
            'author': self.author.username
        }

    @property
    def read_times(self):
        return Count.get('article:{}'.format(self.id))

    @read_times.setter
    def read_times(self, value):
        Count.set('article:{}'.format(self.id))


class Comment(db.Model, ModelUserMixin):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    blog_id = db.Column(
        db.Integer, db.ForeignKey(
            'blog.id', ondelete="CASCADE"))
    blog = db.relationship(
        'Blog',
        backref=db.backref(
            'comments', cascade='all,delete-orphan', lazy='dynamic'))

    def __repr__(self):
        return "<Comment %r>" % self.content


class Question(db.Model, ModelUserMixin):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(48), nullable=False)
    description = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    is_hidden = db.Column(db.Boolean, default=False, nullable=False)

    # __mapper_args__ = {"order_by": created_at.desc()}

    def __repr__(self):
        return "<Question %r>" % self.title

    def __str__(self):
        return self.title
