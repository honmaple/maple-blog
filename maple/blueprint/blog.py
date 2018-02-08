#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: blog.py
# Author: jianglin
# Email: lin.jiang@upai.com
# Created: 2018-02-08 14:42:15 (CST)
# Last Update: 星期五 2018-02-09 17:09:11 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import render_template, request
from flask_maple.views import MethodView
from sqlalchemy import extract
from maple.utils import gen_filter_dict, gen_order_by
from maple.extension import cache
from maple.helper import cache_key
from maple.model import Blog


class BlogListView(MethodView):
    def render_template(self, *args, **kwargs):
        return render_template(*args, **kwargs)

    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        query_dict = request.data
        query_dict['descent'] = 'created_at'
        tag = query_dict.pop('tag', None)
        category = query_dict.pop('category', None)
        author = query_dict.pop('author', None)
        year = query_dict.pop('year', None)
        month = query_dict.pop('month', None)
        if tag is not None:
            query_dict.update(tags__name=tag)
        if category is not None:
            query_dict.update(category__name=category)
        if author is not None:
            query_dict.update(author__name=author)
        page, number = self.pageinfo
        keys = ['title', 'tags__name', 'category__name', 'author__username']
        equal_key = ['tags__name', 'category__name', 'author__username']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key)
        blogs = Blog.query.filter_by(**filter_dict)
        if year is not None:
            blogs = blogs.filter(extract('year', Blog.created_at) == year)
        if month is not None:
            blogs = blogs.filter(extract('month', Blog.created_at) == month)
        blogs = blogs.order_by(*order_by).paginate(page, number)
        data = {'blogs': blogs}
        return self.render_template('blog/itemlist.html', **data)


class BlogView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self, pk):
        blog = Blog.query.filter_by(id=pk).first_or_404()
        '''记录用户浏览次数'''
        blog.read_times = 1
        data = {'blog': blog}
        return render_template('blog/item.html', **data)


class ArchiveView(BlogListView):
    per_page = 30

    def render_template(self, *args, **kwargs):
        return render_template('blog/archives.html', **kwargs)
