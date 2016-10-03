#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-04 00:42:01 (CST)
# Last Update:星期二 2016-10-4 1:2:20 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import (UserInforView, UserPasswordView, UserBlogListView,
                    UserCommentListView, UserQueListView)

site = Blueprint('user', __name__)

site.add_url_rule('/<name>',
                  view_func=UserInforView.as_view('infor'))
site.add_url_rule('/<name>/password',
                  view_func=UserPasswordView.as_view('password'))
site.add_url_rule('/<name>/blog',
                  view_func=UserBlogListView.as_view('blog'))
site.add_url_rule('/<name>/comment',
                  view_func=UserCommentListView.as_view('comment'))
site.add_url_rule('/<name>/question',
                  view_func=UserQueListView.as_view('question'))
