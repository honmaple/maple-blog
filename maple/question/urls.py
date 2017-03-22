#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-03 18:46:34 (CST)
# Last Update:星期三 2017-3-22 14:38:59 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import QueListView, QuePrivateView, QueView

site = Blueprint('question', __name__)

site.add_url_rule('/', view_func=QueListView.as_view('quelist'))
site.add_url_rule('/private', view_func=QuePrivateView.as_view('privatelist'))
site.add_url_rule('/<int:queId>', view_func=QueView.as_view('que'))
