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
from flask_babelex import gettext as _
from maple.extensions import cache
from maple.helper import cache_key
from maple.common.utils import (gen_filter_dict, gen_order_by)
from maple.common.views import BaseMethodView as MethodView
from .models import Books


class BookListView(MethodView):
    per_page = 18

    @cache.cached(timeout=300, key_prefix=cache_key)
    def get(self):
        query_dict = request.data
        page, number = self.page_info
        keys = ['name', 'tag']
        equal_key = ['tag']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key)
        books = Books.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        data = {'title': _('Books - HonMaple'), 'books': books}
        return render_template('book/booklist.html', **data)


class BookView(MethodView):
    @cache.cached(timeout=300, key_prefix=cache_key)
    def get(self, bookId):
        book = Books.query.filter_by(id=bookId).first_or_404()
        data = {
            'title': _('%(name)s - Books - HonMaple', name=book.name),
            'book': book
        }
        return render_template('book/book.html', **data)


class BookTagListView(MethodView):
    @cache.cached(timeout=300)
    def get(self):
        tags = Books.query.distinct(Books.tag)
        data = {'tags': tags}
        return render_template('book/taglist.html', **data)
