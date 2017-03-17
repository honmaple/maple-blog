#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-03 16:28:06 (CST)
# Last Update:星期五 2017-3-17 19:30:0 (CST)
#          By:
# Description:
# **************************************************************************

from flask import Blueprint
from .views import BookListView, BookView, BookTagListView

site = Blueprint('book', __name__, url_prefix='/books')

site.add_url_rule('', view_func=BookListView.as_view('booklist'))
site.add_url_rule('/<int:bookId>', view_func=BookView.as_view('book'))
site.add_url_rule('/tags', view_func=BookTagListView.as_view('taglist'))
