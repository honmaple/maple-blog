#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
# *************************************************************************
from urllib.parse import urljoin

from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_babelex import gettext as _
from flask_login import login_required
from sqlalchemy import extract
from werkzeug.contrib.atom import AtomFeed
from werkzeug.utils import escape

from maple.common.utils import gen_filter_dict, gen_order_by
from maple.common.validator import Validator
from maple.common.views import BaseMethodView as MethodView
from maple.extensions import cache, csrf, db
from maple.helper import cache_key
from maple.utils import superuser_required

from .filters import safe_markdown
from .models import Blog, Category, Comment, Tags


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
        page, number = self.page_info
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
        return self.render_template('blog/bloglist.html', **data)

    decorators = [csrf.exempt]

    @superuser_required
    def post(self):
        validator = Validator('blog')
        validator.add_validator('title', type=str, required=True)
        validator.add_validator('content', type=str, required=True)
        validator.add_validator('category', type=str, required=True)
        validator.add_validator('tags', type=str, required=True)
        post_data = request.data
        v = validator.is_valid(post_data)
        if v is not True:
            return jsonify(status=401, message=v)
        author = request.user
        title = post_data.pop('title', None)
        content = post_data.pop('content', None)
        content_type = Blog.CONTENT_TYPE_MARKDOWN
        is_copy = True if post_data.pop('is_copy', None) else False
        if post_data.pop('content_type', None) in ('markdown', '0', 'md'):
            content_type = Blog.CONTENT_TYPE_MARKDOWN
        else:
            content_type = Blog.CONTENT_TYPE_ORGMODE
        _category = post_data.pop('category', None).capitalize()
        _tags = post_data.pop('tags', None).split(',')
        blog = Blog(
            title=title,
            content=content,
            content_type=content_type,
            is_copy=is_copy,
            author=author)
        for _tag in _tags:
            tag = Tags.query.filter_by(name=_tag).first()
            if not tag:
                tag = Tags(name=_tag)
                tag.save()
            blog.tags.append(tag)
        category = Category.query.filter_by(name=_category).first()
        if not category:
            category = Category(name=_category)
            category.save()
        blog.category = category
        blog.save()
        return jsonify(status='200', message=blog.to_json())


class BlogView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self, blogId):
        blog = Blog.query.filter_by(id=blogId).first_or_404()
        '''记录用户浏览次数'''
        blog.read_times = 1
        data = {'blog': blog}
        return render_template('blog/blog.html', **data)

    decorators = [csrf.exempt]

    @login_required
    def put(self, blogId):
        author = request.user
        post_data = request.data
        blog = Blog.query.filter_by(id=blogId, author=author).first()
        message = 'id is not exists.'
        if not blog:
            return jsonify(status='200', message=message)
        for i in ['title', 'content']:
            arg = post_data.pop(i, None)
            if arg is not None:
                setattr(blog, i, arg)
        _category = post_data.pop('category', None)
        if _category is not None:
            _category = _category.capitalize()
            category = Category.query.filter_by(name=_category).first()
            if not category:
                category = Category(name=_category)
                category.save()
            blog.category = category
        _tags = post_data.pop('tags', '').split(',')
        for _tag in _tags:
            tag = Tags.query.filter_by(name=_tag).first()
            if not tag:
                tag = Tags(name=_tag)
                tag.save()
            blog.tags.append(tag)
        blog.save()
        message = blog.to_json()
        return jsonify(status='200', message=message)

    @login_required
    def delete(self, blogId):
        author = request.user
        blog = Blog.query.filter_by(id=blogId, author=author).first()
        message = 'id is not exists.'
        if blog:
            message = blog.to_json()
            blog.delete()
        return jsonify(status='200', message=message)


class ArchiveView(BlogListView):
    per_page = 30

    def render_template(self, *args, **kwargs):
        return render_template('blog/archives.html', **kwargs)


class RssView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        feed = AtomFeed(
            _("honmaple's Blog"),
            feed_url=request.url,
            url=request.url_root,
            subtitle='I like solitude, yearning for freedom')
        blogs = Blog.query.limit(10)
        for blog in blogs:
            feed.add(blog.title,
                     escape(safe_markdown(blog.content)),
                     content_type='html',
                     author=blog.author.username,
                     url=urljoin(
                         request.url_root,
                         url_for(
                             'blog.blog', blogId=blog.id)),
                     updated=blog.created_at
                     if blog.updated_at is not None else blog.updated_at,
                     published=blog.created_at)
        return feed.get_response()
