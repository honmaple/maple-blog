#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: jinja.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-02-08 15:25:56 (CST)
# Last Update: Monday 2019-06-10 01:00:04 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_babel import format_datetime
from flask_babel import lazy_gettext as _
from datetime import datetime
from maple import default


def timesince(dt, default=_("just now")):
    now = datetime.utcnow()
    diff = now - dt
    if diff.days > 90:
        return format_datetime(dt, 'Y-MM-dd')
    if diff.days > 10:
        return format_datetime(dt, 'Y-MM-dd HH:mm')
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
    app.jinja_env.globals['DEFAULT'] = default
