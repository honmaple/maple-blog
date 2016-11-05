#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
# *************************************************************************
from flask import render_template, request
from flask.views import MethodView
from flask_maple.views import ViewList, View
from flask_babelex import gettext as _
from maple import cache
from .models import Books
from .serializer import BookSerializer


class BookListView(ViewList):
    model = Books
    serializer = BookSerializer
    template = 'book/booklist.html'
    per_page = 18

    def get_filter_dict(self):
        tag = request.args.get('tag')
        filter_dict = {}
        if tag is not None:
            filter_dict.update(tag=tag)
        return filter_dict


class BookView(View):
    model = Books
    serializer = BookSerializer
    template = 'book/book.html'

    @cache.cached(timeout=180)
    def get(self, bookId):
        return super(BookView, self).get(bookId)


class BookTagListView(MethodView):
    @cache.cached(timeout=300)
    def get(self):
        tags = Books.query.distinct(Books.tag)
        data = {'tags': tags}
        return render_template('book/taglist.html', **data)
