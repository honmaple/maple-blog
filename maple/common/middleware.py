#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: middleware.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-19 22:41:42 (CST)
# Last Update:星期二 2017-8-29 16:51:37 (CST)
#          By:
# Description:
# **************************************************************************
import cProfile
import pstats
from io import StringIO

from flask import g, request
from flask_login import current_user


class CProfileMiddleware(object):
    def preprocess_request(self):
        pr = cProfile.Profile()
        pr.enable()
        request.pr = pr

    def process_response(self, response):
        pr = request.pr
        pr.disable()
        s = StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return response


class Middleware(object):
    def preprocess_request(self):
        g.user = current_user
        request.user = current_user._get_current_object()
        if request.method == 'GET':
            request.data = request.args.to_dict()
        else:
            request.data = request.json
            if request.data is None:
                request.data = request.form.to_dict()
