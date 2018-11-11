#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: helper.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-11-26 23:47:44 (CST)
# Last Update: Tuesday 2018-11-06 13:52:23 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request


def cache_key():
    key = request.url
    return 'view:%s' % key
