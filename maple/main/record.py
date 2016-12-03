#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: record.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-03 21:44:43 (CST)
# Last Update:星期六 2016-12-3 22:31:53 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request
from maple.extensions import redis_data as redis


class Record(object):
    def add(self,
            key,
            user_key=lambda: 'user:%s',
            timeout=300):
        if callable(user_key):
            user_key = user_key()
        if '%s' in user_key:
            user_key = user_key % request.remote_addr
        user_key = '%s:%s' % (user_key, key)
        if not redis.exists(user_key):
            redis.set(user_key, 1)
            redis.expire(user_key, timeout)
            redis.zincrby('visited:article', key, 1)

    def get(self, key):
        count = redis.zscore("visited:article", "article:%s" % str(key))
        if count is None:
            count = 0.0
        count = int(count)
        return count


record = Record()
