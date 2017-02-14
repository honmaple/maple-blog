#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: middleware.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-17 22:05:43 (CST)
# Last Update:星期日 2017-2-12 16:31:0 (CST)
#          By:
# Description:
# **************************************************************************
from flask import g
from flask_login import current_user
from flask import g, request, abort, current_app
from sqlalchemy import or_
import re


class CommonMiddleware(object):
    def preprocess_request(self):
        g.user = current_user


class RequestMiddleware(object):
    def preprocess_request(self):
        if request.method == 'GET':
            request.data = request.args.to_dict()
        else:
            request.data = request.form.to_dict()

    def process_response(self, response):
        # if hasattr(request, 'data'):
        #     del request.data
        return response
