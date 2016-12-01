#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: helper.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-26 23:47:44 (CST)
# Last Update:星期日 2016-11-27 0:12:29 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request


def cache_key():
    key = request.url
    return 'view:%s' % key
