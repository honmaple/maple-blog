#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-13 14:52:01 (CST)
# Last Update:星期五 2017-3-17 23:26:55 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint

from .views import TimeLineListView

site = Blueprint('timeline', __name__)
timelinelist_view = TimeLineListView.as_view('timelinelist')
site.add_url_rule('', view_func=timelinelist_view)
