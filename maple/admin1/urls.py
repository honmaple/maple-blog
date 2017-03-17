#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-17 13:56:08 (CST)
# Last Update:星期五 2017-3-17 15:5:55 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import (BlogListView, CategoryListView, TagListView, UserListView)

site = Blueprint('admin1', __name__, url_prefix='/admin')

site.add_url_rule('/blog', view_func=BlogListView.as_view('blog'))
site.add_url_rule('/tag', view_func=TagListView.as_view('tag'))
site.add_url_rule('/category', view_func=CategoryListView.as_view('category'))
site.add_url_rule('/user', view_func=UserListView.as_view('user'))
