#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: count.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-03-10 23:57:07 (CST)
# Last Update: Saturday 2019-05-25 00:01:48 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from maple.extension import redis


class Count(object):
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
            redis.zincrby('count:article:visited', key, 1)

    @classmethod
    def get(cls, key):
        count = redis.zscore("count:article:visited", key)
        if count is None:
            count = 0.0
        count = int(count)
        return count
