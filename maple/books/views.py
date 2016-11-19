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
from flask_babelex import gettext as _
from maple.extensions import cache
from .models import Books


class BookListView(MethodView):
    @cache.cached(timeout=300)
    def get(self):
        page = request.args.get('page', 1, type=int)
        tag = request.args.get('tag')
        filter_dict = {}
        if tag is not None:
            filter_dict.update(tag=tag)
        books = Books.get_book_list(page, filter_dict)
        data = {'title': _('书籍查询 - HonMaple'), 'books': books}
        return render_template('book/booklist.html', **data)


class BookView(MethodView):
    @cache.cached(timeout=180)
    def get(self, bookId):
        book = Books.get(bookId)
        data = {
            'title': _('%(name)s - 书籍查询 - HonMaple', name=book.name),
            'book': book
        }
        return render_template('book/book.html', **data)


class BookTagListView(MethodView):
    @cache.cached(timeout=300)
    def get(self):
        tags = Books.query.distinct(Books.tag)
        data = {'tags': tags}
        return render_template('book/taglist.html', **data)
