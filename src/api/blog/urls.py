#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-03 15:53:46 (CST)
# Last Update:星期二 2017-3-7 21:31:9 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import (BlogListView, BlogView, CommentListView, CategoryListView,
                    TagListView, TimeListView)

site = Blueprint('blog', __name__, url_prefix='/api/blog')
bloglist_view = BlogListView.as_view('bloglist')
blog_view = BlogView.as_view('blog')
site.add_url_rule('/', view_func=bloglist_view)
site.add_url_rule('/<int:blogId>', view_func=blog_view)
site.add_url_rule(
    '/<int:blogId>/comment/', view_func=CommentListView.as_view('comment'))
site.add_url_rule('/category/', view_func=CategoryListView.as_view('category'))
site.add_url_rule('/tag/', view_func=TagListView.as_view('tag'))
site.add_url_rule('/time/', view_func=TimeListView.as_view('time'))
