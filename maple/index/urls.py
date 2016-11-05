#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-03 16:57:33 (CST)
# Last Update:星期六 2016-11-5 13:25:5 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import IndexView, AboutView, RainView, ResumeView

site = Blueprint('index', __name__)

index_view = IndexView.as_view('index')
rain_view = RainView.as_view('rain')
about_view = AboutView.as_view('about')
resume_view = ResumeView.as_view('resume')
site.add_url_rule('/', view_func=index_view)
site.add_url_rule('/index', view_func=index_view)
site.add_url_rule('/rain', view_func=rain_view)
site.add_url_rule('/about', view_func=about_view)
site.add_url_rule('/resume', view_func=resume_view)
