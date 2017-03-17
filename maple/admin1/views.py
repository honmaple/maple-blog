#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-17 13:46:31 (CST)
# Last Update:星期五 2017-3-17 15:6:44 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request, render_template
from maple.common.views import IsAuthMethodView as MethodView
from maple.common.utils import (gen_filter_date, gen_order_by, gen_filter_dict)
from maple.blog.models import Blog, Category, Tags
from maple.user.models import User


class BlogListView(MethodView):
    def get(self):
        query_dict = request.data
        mode = query_dict.pop('mode', None)
        if mode == 'add':
            return self.add()
        user = request.user
        page, number = self.page_info
        keys = ['title', 'content']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, user=user)
        blogs = Blog.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        data = {'blogs': blogs}
        return render_template('admin/blog_list.html', **data)

    def post(self):
        pass

    def add(self):
        return render_template('admin/blog_add.html')


class BlogView(MethodView):
    def get(self, pk):
        query_dict = request.data
        mode = query_dict.pop('mode', None)
        if mode == 'edit':
            return self.edit()

    def edit(self):
        return render_template('admin/blog_edit.html')

    def put(self, pk):
        pass

    def delete(self, pk):
        pass


class CategoryListView(MethodView):
    def get(self):
        query_dict = request.data
        user = request.user
        page, number = self.page_info
        keys = ['name']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys)
        categories = Category.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        return render_template('admin/category_list.html', data=categories)

    def post(self):
        pass


class TagListView(MethodView):
    def get(self):
        query_dict = request.data
        user = request.user
        page, number = self.page_info
        keys = ['name']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys)
        tags = Tags.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        return render_template('admin/tag_list.html', data=tags)

    def post(self):
        pass


class UserListView(MethodView):
    def get(self):
        query_dict = request.data
        page, number = self.page_info
        keys = ['username']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys)
        users = User.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        return render_template('admin/user_list.html', data=users)


class QuestionListView(MethodView):
    def get(self):
        pass
