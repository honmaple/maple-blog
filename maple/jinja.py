#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: jinja.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2018-02-08 15:25:56 (CST)
# Last Update: Sunday 2018-03-11 14:46:31 (CST)
#          By:
# Description:
# ********************************************************************************
from maple.extension import db
from flask import Markup, current_app
from sqlalchemy import func, extract
from misaka import Markdown, HtmlRenderer
from bleach import clean
from itsdangerous import URLSafeSerializer
from orgpython import org_to_html
from datetime import datetime
from .model import Category, Blog, Tag


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
    text = org_to_html(text)
    return Markup(safe_clean(text))


def tag_archives():
    tags = db.session.query(
        Tag, func.count(Blog.id)).outerjoin(Tag.blogs).group_by(Tag.id)
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


def timesince(dt, default="just now"):
    from flask_babel import format_datetime
    now = datetime.utcnow()
    diff = now - dt
    if diff.days > 10:
        return format_datetime(dt, 'Y-M-d H:m')
    elif diff.days <= 10 and diff.days > 0:
        periods = ((diff.days, "day", "days"), )
    elif diff.days <= 0 and diff.seconds > 3600:
        periods = ((diff.seconds / 3600, "hour", "hours"), )
    elif diff.seconds <= 3600 and diff.seconds > 90:
        periods = ((diff.seconds / 60, "minute", "minutes"), )
    else:
        return default

    for period, singular, plural in periods:

        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)

    return default


def init_app(app):
    app.add_template_filter(safe_markdown)
    app.add_template_filter(orgmode)
    app.add_template_filter(timesince)

    app.add_template_global(category_archives)
    app.add_template_global(tag_archives)
    # app.add_template_global(time_archives)
