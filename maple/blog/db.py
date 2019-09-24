#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: db.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 18:38:14 (CST)
# Last Update: Monday 2019-09-09 00:44:34 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import current_app
from flask_babel import format_datetime
from flask_maple.models import ModelMixin, ModelUserMixin
from maple.count import Count
from maple.extension import db
from sqlalchemy import text

from .markup import markdown_to_html, orgmode_to_html


class TimeLine(db.Model, ModelUserMixin):
    __tablename__ = 'timeline'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    is_hidden = db.Column(db.Boolean, nullable=True, default=False)

    __mapper_args__ = {"order_by": text("created_at desc")}

    def __repr__(self):
        return "<TimeLine %r>" % self.content[:10]

    def __str__(self):
        return self.content[:10]

    @property
    def datetime_format(self):
        return format_datetime(self.created_at, 'Y-M-d H:M')

    def to_json(self):
        return {'id': self.id, 'content': self.content, 'hide': self.hide}


article_tags = db.Table(
    'article_tags', db.Column(
        'tag_id',
        db.Integer,
        db.ForeignKey('tag.id'),
    ), db.Column(
        'article_id',
        db.Integer,
        db.ForeignKey('article.id'),
    ))


class Tag(db.Model, ModelMixin):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    articles = db.relationship(
        'Article',
        secondary=article_tags,
        backref=db.backref('tags', lazy='dynamic'),
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


class Article(db.Model, ModelUserMixin):
    __tablename__ = 'article'

    CONTENT_TYPE_MARKDOWN = 0
    CONTENT_TYPE_ORGMODE = 1

    CONTENT_TYPE = ((0, 'markdown'), (1, 'org-mode'))

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_type = db.Column(
        db.Integer, nullable=False, default=CONTENT_TYPE_MARKDOWN)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.id', ondelete="CASCADE"),
        nullable=False)
    category = db.relationship(
        'Category',
        backref=db.backref(
            'articles', cascade='all,delete-orphan', lazy='dynamic'),
        uselist=False,
        lazy='joined')

    __mapper_args__ = {"order_by": text("created_at desc")}

    def __repr__(self):
        return "<Article %r>" % self.title

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category.name,
            'tags': ','.join([tag.name for tag in self.tags]),
        }

    def to_html(self, length=None, truncate=False):
        length = length or current_app.config.get("SUMMARY_MAX_LENGTH")
        if not truncate:
            length = None
        if self.content_type == self.CONTENT_TYPE_MARKDOWN:
            return markdown_to_html(self.content, length)
        return orgmode_to_html(self.content, length)

    @property
    def htmlcontent(self):
        return self.to_html()

    @property
    def next_article(self):
        return Article.query.filter_by(id__lt=self.id).order_by("-id").first()

    @property
    def previous_article(self):
        return Article.query.filter_by(id__gt=self.id).order_by("id").first()

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
    article_id = db.Column(
        db.Integer,
        db.ForeignKey('article.id', ondelete="CASCADE"),
        nullable=False)
    article = db.relationship(
        'Article',
        backref=db.backref(
            'comments', cascade='all,delete-orphan', lazy='dynamic'),
        uselist=False)

    def __repr__(self):
        return "<Comment %r>" % self.content
