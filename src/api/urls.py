#!/usr/bin/env python

# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-02-12 16:12:07 (CST)
# Last Update:星期二 2017-3-7 20:19:25 (CST)
#          By:
# Description:
# **************************************************************************
from .blog.urls import site as blog_site
from .timeline.urls import site as timeline_site
from .books.urls import site as book_site


def api_routers(app):
    app.register_blueprint(blog_site)
    app.register_blueprint(book_site)
    app.register_blueprint(timeline_site)
