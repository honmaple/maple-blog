#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: helper.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-11-26 23:47:44 (CST)
# Last Update: Friday 2018-11-16 16:51:46 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request


def accept_language():
    return request.accept_languages.best_match(['zh', 'en'], 'zh')


def cache_key():
    key = request.url
    lang = accept_language()
    return 'view:{0}:{1}'.format(lang, key)
