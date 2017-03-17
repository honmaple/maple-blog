#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: middleware.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-19 22:41:42 (CST)
# Last Update:星期五 2017-3-17 14:3:52 (CST)
#          By:
# Description:
# **************************************************************************
from flask import g, request, make_response, render_template
from flask_login import current_user
from maple.blog.forms import SearchForm
from time import time
from random import choice
import re


class CommonMiddleware(object):
    def preprocess_request(self):
        g.search_form = SearchForm()
        g.user = current_user
        request.user = current_user._get_current_object()
        if request.method == 'GET':
            request.data = request.args.to_dict()
        else:
            request.data = request.json
            if request.data is None:
                request.data = request.form.to_dict()


class IndexMiddleware(object):
    def preprocess_request(self):
        user_agent = request.headers.get('User-Agent')
        regex = r'bot|spider'
        user_agent = str(user_agent)
        if user_agent is not None and re.findall(regex, user_agent, re.I):
            return
        rain = request.cookies.get('welcome')
        index_templates = ['index/console.html', 'index/rain.html']
        template = choice(index_templates)
        if not rain:
            response = make_response(render_template(template))
            response.set_cookie(
                key='welcome',
                value='Welcome to my Blog',
                expires=time() + 60 * 30)
            return response
