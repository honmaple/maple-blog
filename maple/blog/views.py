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
from flask.views import MethodView
from flask_login import current_user, login_required
from flask_maple.views import BaseView
from maple.extensions import db, redis_data, cache
from maple.blog.forms import CommentForm
from maple.main.permissions import writer_permission
from maple.helper import cache_key
from flask_babelex import gettext as _
from urllib.parse import urljoin
from maple.filters import safe_markdown
from maple.main.record import record
from werkzeug.contrib.atom import AtomFeed
from werkzeug.utils import escape
from .models import Blog, Comment


class BlogListView(BaseView):
    def get_filter_dict(self):
        category = request.args.get('category')
        tag = request.args.get('tag')
        author = request.args.get('author')
        filter_dict = {}
        if category is not None:
            filter_dict.update(category__name=category)
        if tag is not None:
            filter_dict.update(tags__name=tag)
        if author is not None:
            filter_dict.update(author__username=author)
        return filter_dict

    def get_sort_tuple(self):
        orderby = request.args.get('orderby')
        sort_tuple = []
        if orderby in ['id', 'created_at', 'updated_at']:
            sort_tuple.append(orderby)
        sort_tuple = tuple(sort_tuple)
        return sort_tuple

    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        page, number = self.get_page_info()
        filter_dict = self.get_filter_dict()
        sort_tuple = self.get_sort_tuple()
        blogs = Blog.get_list(page, number, filter_dict, sort_tuple)
        data = {'blogs': blogs}
        return render_template('blog/bloglist.html', **data)


class BlogView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self, blogId):
        '''记录用户浏览次数'''
        record.add('article:%s' % str(blogId))
        blog = Blog.get(blogId)
        data = {'blog': blog}
        return render_template('blog/blog.html', **data)


class CommentListView(BaseView):
    # form = CommentForm()

    def __init__(self):
        super(MethodView, self).__init__()
        self.form = CommentForm()

    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self, blogId):
        page, number = self.get_page_info()
        filter_dict = {}
        filter_dict.update(blog_id=blogId)
        comments = Comment.get_list(page, number, filter_dict)
        data = {'comments': comments, 'form': self.form}
        return render_template('blog/commentlist.html', **data)

    @login_required
    def post(self, blogId):
        if not writer_permission.can():
            flash(_('You have not confirm your account'))
            return redirect(url_for('blog.blog', blogId=blogId))
        if self.form.validate_on_submit():
            comment = Comment()
            comment.author = current_user
            comment.content = self.form.content.data
            comment.blog_id = blogId
            db.session.add(comment)
            db.session.commit()
            return redirect(
                url_for(
                    'blog.blog', blogId=blogId, _anchor='blog-comment'))
        return redirect(
            url_for(
                'blog.blog', blogId=blogId, _anchor='blog-comment'))


class BlogArchiveView(BaseView):
    per_page = 30

    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        page, number = self.get_page_info()
        blogs = Blog.get_list(page, number)
        data = {'blogs': blogs}
        return render_template('blog/archives.html', **data)


class BlogRssView(MethodView):
    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        feed = AtomFeed(
            _("HonMaple's Blog"),
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
