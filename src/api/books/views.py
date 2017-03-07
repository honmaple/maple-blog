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
from common.views import BaseMethodView as MethodView
from common.utils import gen_filter_dict, gen_filter_date, gen_order_by
from common.serializer import Serializer, PageInfo
from common.response import HTTPResponse
from .models import Books


class BookListView(MethodView):
    per_page = 18

    def get(self):
        query_dict = request.data
        page, number = self.page_info
        keys = ['tag', 'content']
        equal_key = ['tag']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key)
        books = Books.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        serializer = Serializer(books.items, many=True)
        pageinfo = PageInfo(books)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS,
            data=serializer.data,
            pageinfo=pageinfo).to_response()


class BookView(MethodView):
    # @cache.cached(timeout=300, key_prefix=cache_key)
    def get(self, bookId):
        book = Books.query.filter_by(id=bookId).first()
        if not book:
            msg = '书籍不存在'
            return HTTPResponse(
                HTTPResponse.HTTP_CLOUD_NOT_EXIST, message=msg).to_response()
        serializer = Serializer(book)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS, data=serializer.data).to_response()


class BookTagListView(MethodView):
    # @cache.cached(timeout=300)
    def get(self):
        tags = Books.query.distinct(Books.tag)
        serializer = Serializer(tags, many=True)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS, data=serializer.data).to_response()
