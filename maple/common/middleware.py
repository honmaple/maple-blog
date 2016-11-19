#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: middleware.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-19 22:41:42 (CST)
# Last Update:星期六 2016-11-19 22:56:20 (CST)
#          By:
# Description:
# **************************************************************************
from flask import g
from flask_login import current_user
from maple.blog.forms import SearchForm


class CommonMiddleware(object):
    def preprocess_request(self):
        g.search_form = SearchForm()
        g.user = current_user
