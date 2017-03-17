#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: filters.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-02 12:59:38 (CST)
# Last Update:星期五 2017-3-17 19:47:18 (CST)
#          By:
# Description:
# **************************************************************************
from datetime import datetime
from maple.main.record import record


def encrypt(text):
    from itsdangerous import URLSafeSerializer
    from flask import current_app
    secret_key = current_app.config.get('SECRET_KEY', 'never')
    s = URLSafeSerializer(secret_key)
    return s.dumps(text)


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
    app.jinja_env.filters['visit_total'] = record.get
    app.jinja_env.filters['timesince'] = timesince
    app.jinja_env.filters['encrypt'] = encrypt
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
