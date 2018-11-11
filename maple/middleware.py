#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: middleware.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-02-08 15:20:44 (CST)
# Last Update: Tuesday 2018-11-06 13:52:21 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import g, request
from flask_login import current_user


class Middleware(object):
    def preprocess_request(self):
        g.user = current_user
        request.user = current_user._get_current_object()
        if request.method in ["GET", "DELETE"]:
            request.data = request.args.to_dict()
        else:
            request.data = request.json
            if request.data is None:
                request.data = request.form.to_dict()
