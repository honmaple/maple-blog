#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: blog.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-26 16:07:56 (CST)
# Last Update:星期一 2016-12-12 18:32:54 (CST)
#          By:
# Description:
# **************************************************************************
from .views import BaseModelView
from maple.blog.models import Blog, Comment, Tags, Category
from maple.extensions import db

__all__ = ['register_blog']


class BlogView(BaseModelView):
    # column_exclude_list = ['author']
    column_searchable_list = ['title']
    column_filters = ['category', 'created_at']
    form_widget_args = {'content': {'rows': 10}}
    column_formatters = dict(
        content=lambda v, c, m, p: m.content[:100] + '...',
        content_type=lambda v, c, m, p: m.get_choice_display('content_type', 'CONTENT_TYPE')
    )

    column_editable_list = ['title', 'category', 'is_copy', 'content_type']
    # inline_models = [Tags]
    form_excluded_columns = ['comments']
    form_choices = {'content_type': Blog.CONTENT_TYPE}


class TagView(BaseModelView):
    column_editable_list = ['name']


class CategoryView(BaseModelView):
    column_editable_list = ['name']


class CommentView(BaseModelView):
    column_editable_list = ['author', 'blog']
    column_filters = ['created_at', 'author']


def register_blog(admin):
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
            Tags,
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
