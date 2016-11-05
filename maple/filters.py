#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: filters.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-02 12:59:38 (CST)
# Last Update:星期六 2016-11-5 12:30:59 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Markup
from misaka import Markdown, HtmlRenderer
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from bleach import clean
from datetime import datetime


def safe_clean(text):
    tags = ['b', 'i', 'font', 'br', 'blockquote', 'div', 'h2', 'ul', 'li', 'a']
    attrs = {'*': ['style', 'id', 'class'], 'font': ['color'], 'a': ['href']}
    styles = ['color']
    return Markup(clean(text, tags=tags, attributes=attrs, styles=styles))


def safe_markdown(text):
    class HighlighterRenderer(HtmlRenderer):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def blockcode(self, text, lang):
            if not lang:
                return '\n<pre><code>{}</code></pre>\n'.format(text.strip())
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = HtmlFormatter(linenos=True)

            return highlight(text, lexer, formatter)

    renderer = HighlighterRenderer()
    md = Markdown(renderer, extensions=('fenced-code', ))
    return Markup(md(safe_clean(text)))


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


def visit_total(article_id):
    '''文章浏览次数'''
    from maple.main.mark_record import get_article_count
    return get_article_count(article_id)


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
    app.jinja_env.filters['visit_total'] = visit_total
    app.jinja_env.filters['timesince'] = timesince
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
