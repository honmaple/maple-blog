#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-08-08 15:08:36 (CST)
# Last Update:星期一 2016-8-8 15:11:36 (CST)
#          By:
# Description:
# **************************************************************************
from maple.index.views import site as index_site
from maple.user.views import site as user_site
from maple.blog.views import site as blog_site
from maple.question.views import site as question_site
from maple.books.views import site as book_site


def register_urls(app):
    app.register_blueprint(index_site, url_prefix='')
    app.register_blueprint(user_site, url_prefix='/u')
    app.register_blueprint(blog_site, url_prefix='/blog')
    app.register_blueprint(question_site, url_prefix='/question')
    app.register_blueprint(book_site, url_prefix='/books')
    import maple.auth.auth
    import maple.admin.admin
