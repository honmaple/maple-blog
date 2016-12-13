#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-03 15:53:46 (CST)
# Last Update:星期二 2016-12-13 15:16:38 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import (BlogListView, BlogView, BlogRssView, BlogArchiveView,
                    CommentListView)

site = Blueprint('blog', __name__)
bloglist_view = BlogListView.as_view('bloglist')
site.add_url_rule('', view_func=bloglist_view)
site.add_url_rule('/', view_func=bloglist_view)
site.add_url_rule('/<int:blogId>', view_func=BlogView.as_view('blog'))
site.add_url_rule(
    '/<int:blogId>/comment', view_func=CommentListView.as_view('commentlist'))
site.add_url_rule('/archives', view_func=BlogArchiveView.as_view('archive'))
site.add_url_rule('/rss', view_func=BlogRssView.as_view('rss'))
