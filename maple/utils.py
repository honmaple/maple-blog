#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: utils.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-02-08 15:04:16 (CST)
# Last Update: Monday 2019-09-23 16:57:49 (CST)
#          By:
# Description:
# ********************************************************************************
import hashlib
from datetime import datetime
from functools import wraps

from flask import request
from flask_maple.response import HTTP
from flask_maple.views import MethodView as _MethodView
from flask_login import login_required
from maple.extension import cache


class MethodView(_MethodView):
    cache_time = 180

    def dispatch_request(self, *args, **kwargs):
        f = super(MethodView, self).dispatch_request
        if self.cache_time and request.method in ["GET", "HEAD"]:
            return cache.cached(
                timeout=self.cache_time,
                key_prefix=cache_key,
            )(f)(*args, **kwargs)
        return f(*args, **kwargs)


class AuthMethodView(MethodView):
    decorators = (login_required, )


def accept_language():
    return request.accept_languages.best_match(['zh', 'en'], 'zh')


def cache_key():
    key = 'view:{0}:{1}'.format(accept_language, request.url)
    return str(hashlib.md5(key.encode("UTF-8")).hexdigest())


def gen_order_by(query_dict=dict(), keys=[], date_key=True):
    keys.append('id')
    if date_key:
        keys += ['created_at', 'updated_at']
    order_by = ['id']
    descent = query_dict.pop('descent', None)
    if descent is not None:
        descent = descent.split(',')
        descent = list(set(keys) & set(descent))
        order_by = ['-%s' % i for i in descent]
    return tuple(order_by)


def update_maybe(ins, request_data, columns):
    for column in columns:
        value = request_data.get(column)
        if value:
            setattr(ins, column, value)
    return ins


def filter_maybe(request_data, columns, params=None):
    if params is None:
        params = dict()
    is_dict = isinstance(columns, dict)
    for column in columns:
        value = request_data.get(column)
        if not value:
            continue
        key = column if not is_dict else columns.get(column, column)

        if key in ["created_at__gte", "created_at__lte"]:
            value = datetime.strptime(value, '%Y-%m-%d')
        params.update({key: value})
    return params


def check_params(keys, req=None):
    '''
    only check is not NULL
    '''
    def _check_params(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            if req is not None:
                request_data = req
            else:
                request_data = request.data
            for key in keys:
                if not request_data.get(key):
                    return HTTP.BAD_REQUEST(message='{0} required'.format(key))
            return func(*args, **kwargs)

        return decorator

    return _check_params


def is_true(value):
    if isinstance(value, str):
        return value == "1" or value == "True" or value == "true"
    return bool(value)


def lazyconf(app, config, key):
    variables = [item for item in dir(config) if not item.startswith("__")]
    for k, v in app.config.get(key, dict()).items():
        if k not in variables:
            continue
        setattr(config, k, v)
