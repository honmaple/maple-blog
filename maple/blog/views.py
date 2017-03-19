#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
# *************************************************************************
from flask import (render_template, request, redirect, url_for, flash)
from flask_login import login_required
from maple.extensions import db, cache
from maple.blog.forms import CommentForm
from maple.helper import cache_key
from flask_babelex import gettext as _
from urllib.parse import urljoin
from maple.main.record import record
from maple.common.views import BaseMethodView as MethodView
from maple.common.utils import (gen_filter_dict, gen_order_by)
from .models import Blog, Comment
from .filters import safe_markdown
from sqlalchemy import extract
from werkzeug.contrib.atom import AtomFeed
from werkzeug.utils import escape


class BlogListView(MethodView):
    def render_template(self, *args, **kwargs):
        return render_template(*args, **kwargs)

    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        query_dict = request.data
        user = request.user
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


class BlogView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self, blogId):
        '''记录用户浏览次数'''
        record.add('article:%s' % str(blogId))
        blog = Blog.query.filter_by(id=blogId).first_or_404()
        data = {'blog': blog}
        return render_template('blog/blog.html', **data)


class CommentListView(MethodView):
    @login_required
    def post(self, blogId):
        user = request.user
        form = CommentForm()
        if form.validate_on_submit():
            comment = Comment()
            comment.content = form.content.data
            comment.blog_id = blogId
            comment.author = user
            db.session.add(comment)
            db.session.commit()
            return redirect(
                url_for(
                    'blog.blog', blogId=blogId, _anchor='blog-comment'))
        return redirect(
            url_for(
                'blog.blog', blogId=blogId, _anchor='blog-comment'))


class BlogArchiveView(BlogListView):
    per_page = 30

    def render_template(self, *args, **kwargs):
        return render_template('blog/archives.html', **kwargs)


class BlogRssView(MethodView):
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
