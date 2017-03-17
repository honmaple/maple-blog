#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-17 13:51:57 (CST)
# Last Update:星期五 2017-3-17 13:51:59 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request, current_app
from flask.views import MethodView
from flask_login import login_required


class BaseMethodView(MethodView):
    @property
    def page_info(self):
        page = request.args.get('page', 1, type=int)
        if hasattr(self, 'per_page'):
            per_page = getattr(self, 'per_page')
        else:
            per_page = current_app.config.setdefault('PER_PAGE', 20)

        number = request.args.get('number', per_page, type=int)
        if number > 100:
            number = per_page
        return page, number


class IsAuthMethodView(BaseMethodView):
    decorators = [login_required]
