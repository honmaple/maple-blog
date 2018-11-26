#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: blog.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-11-26 16:07:56 (CST)
# Last Update: Monday 2018-11-26 11:48:12 (CST)
#          By:
# Description:
# **************************************************************************
from .views import AdminView
from maple.model import Blog, Comment, Tag, Category
from maple.extension import db


class BlogView(AdminView):
    # column_exclude_list = ['user']
    column_searchable_list = ['title']
    column_filters = ['category', 'created_at']
    form_widget_args = {'content': {'rows': 10}}
    column_formatters = dict(
        content=lambda v, c, m, p: m.content[:100] + '...'
    )

    column_editable_list = ['title', 'category', 'is_copy', 'content_type']
    # inline_models = [Tags]
    form_excluded_columns = ['comments']
    form_choices = {'content_type': Blog.CONTENT_TYPE}


class TagView(AdminView):
    column_editable_list = ['name']


class CategoryView(AdminView):
    column_editable_list = ['name']


class CommentView(AdminView):
    column_editable_list = ['user', 'blog']
    column_filters = ['created_at', 'user']


def init_admin(admin):
    admin.add_view(
        BlogView(
            Blog,
            db.session,
            name='管理文章',
            endpoint='admin_article',
            category='管理博客'))
    admin.add_view(
        CategoryView(
            Category,
            db.session,
            name='管理分类',
            endpoint='admin_category',
            category='管理博客'))
    admin.add_view(
        TagView(
            Tag,
            db.session,
            name='管理节点',
            endpoint='admin_tag',
            category='管理博客'))
    admin.add_view(
        CommentView(
            Comment,
            db.session,
            name='管理回复',
            endpoint='admin_comment',
            category='管理博客'))
