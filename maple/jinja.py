#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: jinja.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-02-08 15:25:56 (CST)
# Last Update: Tuesday 2018-11-13 10:47:02 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_babel import format_datetime
from sqlalchemy import func
from datetime import datetime
from maple.extension import db
from maple.model import Category, Blog, Tag


class Archives:
    def categories():
        ins = db.session.query(Category, func.count(Blog.id)).outerjoin(
            Category.blogs).group_by(Category.id)
        return ins

    def tags():
        ins = db.session.query(Tag, func.count(Blog.id)).outerjoin(
            Tag.blogs).group_by(Tag.id)
        return ins


def timesince(dt, default="just now"):
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
    app.add_template_filter(timesince)
    app.add_template_global(Archives)
