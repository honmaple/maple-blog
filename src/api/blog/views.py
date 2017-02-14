#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
# *************************************************************************
from flask import request
from flask_login import current_user
from common.views import BaseMethodView as MethodView
from common.utils import gen_filter_dict, gen_filter_date, gen_order_by
from common.response import HTTPResponse
from common.serializer import Serializer, PageInfo
from .models import Blog, Comment, Category, Tags


class BlogListView(MethodView):
    def get(self):
        query_dict = request.data
        tag = query_dict.pop('tag', None)
        category = query_dict.pop('category', None)
        author = query_dict.pop('author', None)
        if tag is not None:
            query_dict.update(tags__name=tag)
        if category is not None:
            query_dict.update(category__name=category)
        if author is not None:
            query_dict.update(author__name=author)
        page, number = self.page_info
        keys = ['title', 'tags__name', 'category__name', 'author__username']
        equal_key = ['tags__name', 'category__name', 'author__username']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key,
                                      current_user)
        blogs = Blog.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        serializer = Serializer(blogs.items, many=True)
        pageinfo = PageInfo(blogs)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS,
            data=serializer.data,
            pageinfo=pageinfo).to_response()


class BlogView(MethodView):
    def get(self, blogId):
        blog = Blog.query.filter_by(id=blogId).first()
        if not blog:
            msg = '用户不存在'
            return HTTPResponse(
                HTTPResponse.HTTP_CLOUD_NOT_EXIST, message=msg).to_response()
        serializer = Serializer(blog)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS, data=serializer.data).to_response()

# class BlogRssView(MethodView):
#     @cache.cached(timeout=180, key_prefix=cache_key)
#     def get(self):
#         feed = AtomFeed(
#             _("HonMaple's Blog"),
#             feed_url=request.url,
#             url=request.url_root,
#             subtitle='I like solitude, yearning for freedom')
#         blogs = Blog.query.limit(10)
#         for blog in blogs:
#             feed.add(blog.title,
#                      escape(safe_markdown(blog.content)),
#                      content_type='html',
#                      author=blog.author.username,
#                      url=urljoin(
#                          request.url_root,
#                          url_for(
#                              'blog.blog', blogId=blog.id)),
#                      updated=blog.created_at
#                      if blog.updated_at is not None else blog.updated_at,
#                      published=blog.created_at)
#         return feed.get_response()


class CommentListView(MethodView):
    def get(self, blogId):
        query_dict = request.data
        page, number = self.page_info
        keys = ['content']
        equal_key = []
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key,
                                      current_user)
        comments = Comment.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        serializer = Serializer(comments.items, many=True)
        pageinfo = PageInfo(comments)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS,
            data=serializer.data,
            pageinfo=pageinfo).to_response()


class CategoryListView(MethodView):
    def get(self):
        query_dict = request.data
        page, number = self.page_info
        keys = ['name']
        equal_key = []
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key,
                                      current_user)
        categories = Category.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        serializer = Serializer(categories.items, many=True)
        pageinfo = PageInfo(categories)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS,
            data=serializer.data,
            pageinfo=pageinfo).to_response()


class TagListView(MethodView):
    def get(self):
        query_dict = request.data
        page, number = self.page_info
        keys = ['name']
        equal_key = []
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key,
                                      current_user)
        tags = Tags.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        serializer = Serializer(tags.items, many=True)
        pageinfo = PageInfo(tags)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS,
            data=serializer.data,
            pageinfo=pageinfo).to_response()
