#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: admin.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-11-26 16:07:56 (CST)
# Last Update: Thursday 2019-07-11 18:13:01 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Markup, url_for
from maple.admin import AdminView
from maple.extension import db

from .db import Article, Category, Comment, Tag, TimeLine


class ArticleView(AdminView):
    def _title(view, context, model, name):
        return Markup('<a href="%s" target="_blank">%s</a>' % (url_for(
            "blog.article", pk=model.id), model.title))

    def _content_type(view, context, model, name):
        return dict(Article.CONTENT_TYPE)[model.content_type]

    column_filters = ['category', 'created_at']
    column_exclude_list = ["content", "created_at"]
    column_searchable_list = ['title']
    column_editable_list = ['category', 'content_type']
    column_formatters = {
        "title": _title,
        "content_type": _content_type,
    }

    # inline_models = [Tag]
    form_widget_args = {'content': {'rows': 10}}
    form_excluded_columns = ['comments']
    form_choices = {
        'content_type': [(str(i[0]), i[1]) for i in Article.CONTENT_TYPE]
    }


class TagView(AdminView):
    column_editable_list = ['name']
    column_searchable_list = ['name']


class CategoryView(AdminView):
    column_editable_list = ['name']
    column_searchable_list = ['name']


class CommentView(AdminView):
    column_editable_list = ['user', 'article']
    column_filters = ['created_at', 'user']


class TimeLineView(AdminView):
    column_editable_list = ['is_hidden', 'user']
    column_filters = ['created_at', 'user']
    form_widget_args = {'content': {'rows': 10}}


def init_admin(admin):
    admin.add_view(
        ArticleView(
            Article,
            db.session,
            name='管理文章',
            category='管理博客',
        ))
    admin.add_view(
        CategoryView(
            Category,
            db.session,
            name='管理分类',
            category='管理博客',
        ))
    admin.add_view(TagView(
        Tag,
        db.session,
        name='管理标签',
        category='管理博客',
    ))
    admin.add_view(
        CommentView(
            Comment,
            db.session,
            name='管理回复',
            category='管理博客',
        ))
    admin.add_view(
        TimeLineView(
            TimeLine,
            db.session,
            name='管理时间轴',
            endpoint='admin_timeline',
            category='管理博客'))
