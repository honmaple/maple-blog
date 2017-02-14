#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: redis_client.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-01-11 21:16:04 (CST)
# Last Update:星期三 2017-1-11 21:39:55 (CST)
#          By:
# Description:
# **************************************************************************
from cloud.extensions import redis_client

CAPTCHA_KEY = 'captcha:%s'


class CaptchaClient(object):
    @classmethod
    def get(cls, token):
        key = CAPTCHA_KEY % token
        return redis_client.get(key)

    @classmethod
    def set(cls, token, value, timeout=60):
        key = CAPTCHA_KEY % token
        redis_client.set(key, value)
        redis_client.expire(key, timeout)

    @classmethod
    def get_or_set(cls, token, value, timeout=60):
        val = cls.get(token)
        if not val:
            cls.set(token, value, timeout=60)
        return value
