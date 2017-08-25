#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: utils.py
# Author: jianglin
# Email: lin.jiang@upai.com
# Created: 2017-08-25 16:17:26 (CST)
# Last Update:星期五 2017-8-25 16:19:25 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request
from maple.extensions import redis_data as redis


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
