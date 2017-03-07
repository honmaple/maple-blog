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
from maple.extensions import db
from common.views import BaseMethodView as MethodView
from common.utils import gen_filter_dict, gen_filter_date, gen_order_by
from common.response import HTTPResponse
from common.serializer import Serializer, PageInfo
from .models import Blog, Comment, Category, Tags
from sqlalchemy import func, extract


class BlogListView(MethodView):
    def get(self):
        query_dict = request.data
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
        page, number = self.page_info
        keys = ['title', 'tags__name', 'category__name', 'author__username']
        equal_key = ['tags__name', 'category__name', 'author__username']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key,
                                      current_user)
        blogs = Blog.query.filter_by(**filter_dict)
        if year is not None:
            blogs = blogs.filter(extract('year', Blog.created_at) == year)
        if month is not None:
            blogs = blogs.filter(extract('month', Blog.created_at) == month)
        blogs = blogs.order_by(*order_by).paginate(page, number)
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
            msg = '文章不存在'
            return HTTPResponse(
                HTTPResponse.HTTP_CLOUD_NOT_EXIST, message=msg).to_response()
        serializer = Serializer(blog)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS, data=serializer.data).to_response()


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


class TimeListView(MethodView):
    def get(self):
        times = db.session.query(
            extract('year', Blog.created_at).label('y'),
            extract('month', Blog.created_at).label('m'),
            func.count("*")).group_by('y', 'm').all()
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS, data=times).to_response()


class CategoryListView(MethodView):
    def get(self):
        categories = db.session.query(Category, func.count(Blog.id)).outerjoin(
            Category.blogs).group_by(Category.id).all()
        data = []
        for category, count in categories:
            c = {'id': category.id, 'name': category.name, 'count': count}
            data.append(c)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS, data=data).to_response()


class TagListView(MethodView):
    def get(self):
        tags = db.session.query(
            Tags,
            func.count(Blog.id)).outerjoin(Tags.blogs).group_by(Tags.id).all()
        data = []
        for tag, count in tags:
            c = {'id': tag.id, 'name': tag.name, 'count': count}
            data.append(c)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS, data=data).to_response()
