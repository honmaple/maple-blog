#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: filters.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-02 12:59:38 (CST)
# Last Update:星期二 2016-10-4 14:23:46 (CST)
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
    tags = ['b', 'i', 'font', 'br', 'blockquote', 'div', 'h2', 'ul', 'li', 'a',
            'href']
    attrs = {'*': ['style', 'id', 'class'], 'font': ['color']}
    styles = ['color']
    return Markup(clean(text, tags=tags, attributes=attrs, styles=styles))


def safe_markdown(text):
    class HighlighterRenderer(HtmlRenderer):
        def blockcode(self, text, lang):
            lang = 'python'
            if not lang:
                return '\n<pre><code>{}</code></pre>\n'.format(text.strip())
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = HtmlFormatter()
            return highlight(text, lexer, formatter)

    renderer = HighlighterRenderer()
    md = Markdown(renderer, extensions=('fenced-code', ))
    return Markup(md(safe_clean(text)))
    # return Markup(md(text))


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


def register_jinja2(app):
    def visit_total(article_id):
        '''文章浏览次数'''
        from maple.main.mark_record import get_article_count
        return get_article_count(article_id)

    def last_online_time(ip):
        from maple.main.mark_record import get_user_last_activity
        ip = str(ip, 'utf-8')
        return get_user_last_activity(ip)

    def visited_time(ip):
        from maple.main.mark_record import get_visited_time
        ip = str(ip, 'utf-8')
        return get_visited_time(ip)

    def visited_last_time(ip):
        from maple.main.mark_record import get_visited_last_time
        ip = str(ip, 'utf-8')
        return get_visited_last_time(ip)

    def visited_pages(ip):
        from maple.main.mark_record import get_visited_pages
        ip = str(ip, 'utf-8')
        return get_visited_pages(ip)

    def query_ip(ip):
        from IP import find
        return find(ip)

    def get_all_tags():
        from maple.blog.models import Tags
        tags = Tags.query.distinct(Tags.name).all()
        return tags

    def get_all_category():
        from maple.blog.models import Category
        categories = Category.query.distinct(Category.name).all()
        return categories

    app.jinja_env.globals['get_all_tags'] = get_all_tags
    app.jinja_env.globals['get_all_category'] = get_all_category
    app.jinja_env.filters['safe_markdown'] = safe_markdown
    app.jinja_env.filters['visit_total'] = visit_total
    app.jinja_env.filters['last_online_time'] = last_online_time
    app.jinja_env.filters['visited_time'] = visited_time
    app.jinja_env.filters['visited_last_time'] = visited_last_time
    app.jinja_env.filters['visited_pages'] = visited_pages
    app.jinja_env.filters['query_ip'] = query_ip
    app.jinja_env.filters['timesince'] = timesince
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
