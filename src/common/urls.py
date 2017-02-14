#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-01-13 16:01:58 (CST)
# Last Update:星期二 2017-1-17 16:53:28 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import HTTPCodeListView, ModelChoiceListView

site = Blueprint('common', __name__, url_prefix='/common')

code_list = HTTPCodeListView.as_view('code')
choice_list = ModelChoiceListView.as_view('choice')

site.add_url_rule('/codes', view_func=code_list)
site.add_url_rule('/choices', view_func=choice_list)
# site.add_url_rule('/', view_func=rule_list)
