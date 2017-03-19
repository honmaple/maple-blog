#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: filters.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-17 19:39:37 (CST)
# Last Update:星期六 2017-3-18 23:48:52 (CST)
#          By:
# Description:
# **************************************************************************
from maple.extensions import db
from flask import Markup, current_app
from sqlalchemy import func, extract
from misaka import Markdown, HtmlRenderer
from bleach import clean
from fortune import fortune
from itsdangerous import URLSafeSerializer
from org import org_to_html
from .models import Category, Blog, Tags


def safe_clean(text):
    tags = ['b', 'i', 'font', 'br', 'div', 'h2', 'blockquote', 'ul', 'li', 'a',
            'p', 'strong', 'span', 'h1', 'pre', 'code', 'img', 'h3', 'h4',
            'em', 'hr', 'ol', 'h5', 'table', 'colgroup', 'col', 'th', 'td',
            'tr', 'tbody', 'thead']
    attrs = {
        '*': ['style', 'id', 'class'],
        'font': ['color'],
        'a': ['href'],
        'img': ['src', 'alt']
    }
    styles = ['color']
    return clean(text, tags=tags, attributes=attrs, styles=styles)


def encrypt(text):
    secret_key = current_app.config.get('SECRET_KEY', 'never')
    s = URLSafeSerializer(secret_key)
    return s.dumps(text)


def safe_markdown(text):
    renderer = HtmlRenderer()
    md = Markdown(renderer, extensions=('fenced-code', ))
    return Markup(safe_clean(md(text)))


def markdown(text):
    renderer = HtmlRenderer()
    md = Markdown(renderer, extensions=('fenced-code', ))
    return Markup(md(text))


def orgmode(text):
    text = org_to_html(text).to_html()
    return Markup(safe_clean(text))


def random_fortune():
    return fortune.show()


def tag_archives():
    tags = db.session.query(
        Tags, func.count(Blog.id)).outerjoin(Tags.blogs).group_by(Tags.id)
    return tags.all()


def category_archives():
    categories = db.session.query(
        Category,
        func.count(Blog.id)).outerjoin(Category.blogs).group_by(Category.id)
    return categories.all()


def time_archives():
    times = db.session.query(
        extract('year', Blog.created_at).label('y'),
        extract('month', Blog.created_at).label('m'),
        func.count("*")).group_by('y', 'm')
    return times.all()
