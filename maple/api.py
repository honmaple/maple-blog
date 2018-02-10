#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2018 jianglin
# File Name: api.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2018-01-08 14:24:18 (CST)
# Last Update: 星期六 2018-02-10 13:44:50 (CST)
#          By:
# Description:
# **************************************************************************
from .model import (Blog, Category, Tag, User, Group, Permission, TimeLine,
                    Question)
from .extension import api
from functools import wraps
from flask import request, abort


def require_logined(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method not in ['GET']:
            abort(403)
        return func(*args, **kwargs)

    return decorated_view


def init_app(app):
    api.create_api(Blog, decorators=[require_logined])
    api.create_api(Category)
    api.create_api(Tag)

    api.create_api(User, decorators=[require_logined])
    api.create_api(Group)
    api.create_api(Permission)

    api.create_api(TimeLine)
    api.create_api(Question)
