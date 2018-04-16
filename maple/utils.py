#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: utils.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-25 16:17:26 (CST)
# Last Update: 星期一 2018-02-05 13:34:41 (CST)
#          By:
# Description:
# **************************************************************************
from functools import wraps
from flask import request, abort
from flask_login import login_required, current_user
from maple.extensions import redis_data as redis


def superuser_required(func):
    @wraps(func)
    def _superuser_required(*args, **kwargs):
        @login_required
        def _required():
            if not current_user.is_superuser:
                abort(403)
            return func(*args, **kwargs)

        return _required()

    return _superuser_required


class Record(object):
    @classmethod
    def set(cls, key, user_key=lambda: 'user:%s', timeout=300):
        if callable(user_key):
            user_key = user_key()
        if '%s' in user_key:
            user_key = user_key % request.remote_addr
        user_key = '%s:%s' % (user_key, key)
        if not redis.exists(user_key):
            redis.set(user_key, 1)
            redis.expire(user_key, timeout)
            redis.zincrby('visited:article', key, 1)

    @classmethod
    def get(cls, key):
        count = redis.zscore("visited:article", "article:%s" % str(key))
        if count is None:
            count = 0.0
        count = int(count)
        return count
