#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: filters.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-02 12:59:38 (CST)
# Last Update:星期日 2016-12-4 12:19:5 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Markup
from misaka import Markdown, HtmlRenderer
from bleach import clean
from datetime import datetime
from maple.main.record import record


def safe_clean(text):
    tags = ['b', 'i', 'font', 'br', 'div', 'h2', 'blockquote', 'ul', 'li', 'a',
            'p', 'strong', 'span', 'h1', 'pre', 'code', 'img', 'h3', 'h4',
            'em', 'hr', 'ol', 'h5']
    attrs = {
        '*': ['style', 'id', 'class'],
        'font': ['color'],
        'a': ['href'],
        'img': ['src', 'alt']
    }
    styles = ['color']
    return clean(text, tags=tags, attributes=attrs, styles=styles)


def safe_markdown(text):
    renderer = HtmlRenderer()
    md = Markdown(renderer, extensions=('fenced-code', ))
    return Markup(safe_clean(md(text)))


def markdown(text):
    renderer = HtmlRenderer()
    md = Markdown(renderer, extensions=('fenced-code', ))
    return Markup(md(text))


def timesince(dt, default="just now"):
    from flask_babelex import format_datetime
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


def get_all_tags():
    from maple.blog.models import Tags
    tags = Tags.query.distinct(Tags.name).all()
    return tags


def get_all_category():
    from maple.blog.models import Category
    categories = Category.query.distinct(Category.name).all()
    return categories


def register_jinja2(app):

    app.jinja_env.globals['get_all_tags'] = get_all_tags
    app.jinja_env.globals['get_all_category'] = get_all_category
    app.jinja_env.filters['safe_markdown'] = safe_markdown
    app.jinja_env.filters['markdown'] = markdown
    app.jinja_env.filters['visit_total'] = record.get
    app.jinja_env.filters['timesince'] = timesince
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
