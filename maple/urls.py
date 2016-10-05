#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-08-08 15:08:36 (CST)
# Last Update:星期三 2016-10-5 15:16:7 (CST)
#          By:
# Description:
# **************************************************************************
from maple.index.urls import site as index_site
from maple.user.urls import site as user_site
from maple.blog.urls import site as blog_site
from maple.question.urls import site as question_site
from maple.books.urls import site as book_site


def register_urls(app):
    app.register_blueprint(index_site, url_prefix='')
    app.register_blueprint(user_site, url_prefix='/u')
    app.register_blueprint(blog_site, url_prefix='/blog')
    app.register_blueprint(question_site, url_prefix='/question')
    app.register_blueprint(book_site, url_prefix='/books')
    import maple.auth.auth
    import maple.admin.admin
