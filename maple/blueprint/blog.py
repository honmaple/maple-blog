#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: blog.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-02-08 14:42:15 (CST)
# Last Update: Saturday 2018-11-11 22:27:27 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from flask_maple.views import MethodView
from maple.utils import filter_maybe
from maple.extension import cache
from maple.response import HTTP
from maple.helper import cache_key
from maple.model import Blog


class BlogListView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        request_data = request.data
        page, number = self.pageinfo
        kwargs = filter_maybe(
            request_data, {
                "tag": "tags__name",
                "category": "category__name",
                "author": "author__name",
                "title": "title__contains",
                "year": "created_at__year",
                "month": "created_at__month"
            })
        order_by = ("-created_at", )

        ins = Blog.query.filter_by(**kwargs).order_by(*order_by).paginate(
            page, number)
        return HTTP.HTML('blog/itemlist.html', blogs=ins)


class BlogView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self, pk):
        ins = Blog.query.filter_by(id=pk).first_or_404()
        '''记录用户浏览次数'''
        ins.read_times = 1
        data = {'blog': ins}
        return HTTP.HTML('blog/item.html', **data)


class ArchiveView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        request_data = request.data
        kwargs = filter_maybe(
            request_data, {
                "tag": "tags__name",
                "category": "category__name",
                "author": "author__name",
                "title": "title__contains",
                "year": "created_at__year",
                "month": "created_at__month"
            })
        order_by = ("-created_at", )

        ins = {}
        for blog in Blog.query.filter_by(**kwargs).order_by(*order_by):
            date = blog.created_at.strftime("%Y年%m月")
            ins.setdefault(date, [])
            ins[date].append(blog)
        return HTTP.HTML('blog/archives.html', blogs=ins)
