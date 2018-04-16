#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: middleware.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-25 16:37:29 (CST)
# Last Update: 星期一 2018-02-05 13:34:41 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request, make_response, render_template
from time import time
from random import choice
import re


class Middleware(object):
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
