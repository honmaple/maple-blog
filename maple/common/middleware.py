#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: middleware.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-19 22:41:42 (CST)
# Last Update:星期五 2017-8-25 16:41:37 (CST)
#          By:
# Description:
# **************************************************************************
from flask import g, request
from flask_login import current_user


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
