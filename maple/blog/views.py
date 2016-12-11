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
from maple.extensions import db, redis_data, cache, csrf
from maple.blog.forms import CommentForm
from maple.main.permissions import writer_permission
from maple.helper import cache_key
from flask_babelex import gettext as _
from urllib.parse import urljoin
from maple.filters import safe_markdown
from maple.main.record import record
from werkzeug.contrib.atom import AtomFeed
from werkzeug.utils import escape
from .models import Blog, Comment, Category, Tags


class BlogListView(BaseView):
    decorators = [csrf.exempt]

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

    @login_required
    def post(self):
        if not current_user.is_superuser:
            return 'forbidden'
        post_data = request.get_json()
        title = post_data.pop('title', None)
        content = post_data.pop('content', None)
        is_copy = post_data.pop('is_copy', None)
        tags = post_data.pop('tags', None)
        category = post_data.pop('category', None)
        if title is None:
            return 'title is None'
        if content is None:
            return 'content is None'
        if tags is None:
            return 'tags is None'
        if category is None:
            return 'category is None'
        blog_title = Blog.query.filter_by(title=title).first()
        if blog_title is not None:
            return 'title is existed'
        is_copy = True if is_copy == 'True' else False
        blog_tags = []
        tags = tags.split(',')
        for t in tags:
            tag = Tags.query.filter_by(name=t).first()
            if tag is None:
                tag = Tags()
                tag.name = t
                tag.save()
            blog_tags.append(tag)
        blog_category = Category.query.filter_by(name=category).first()
        if blog_category is None:
            blog_category = Category()
            blog_category.name = category
            blog_category.save()
        blog = Blog()
        blog.title = title
        blog.content = content
        blog.author = current_user
        blog.is_copy = is_copy
        blog.category = blog_category
        blog.tags = blog_tags
        blog.save()
        return 'success'


class BlogView(MethodView):
    decorators = [csrf.exempt]

    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self, blogId):
        '''记录用户浏览次数'''
        record.add('article:%s' % str(blogId))
        blog = Blog.get(blogId)
        data = {'blog': blog}
        return render_template('blog/blog.html', **data)

    @login_required
    def put(self, blogId):
        if not current_user.is_superuser:
            return 'forbidden'
        blog = Blog.query.filter_by(id=blogId).first()
        if blog is None:
            return 'blog is not exist'
        post_data = request.get_json()
        title = post_data.pop('title', None)
        content = post_data.pop('content', None)
        tags = post_data.pop('tags', None)
        category = post_data.pop('category', None)
        if title is not None:
            blog.title = title
        if content is not None:
            blog.content = content
        if tags is not None:
            blog_tags = []
            tags = tags.split(',')
            for t in tags:
                tag = Tags.query.filter_by(name=t).first()
                if tag is None:
                    tag = Tags()
                    tag.name = t
                    tag.save()
                blog_tags.append(tag)
            blog.tags = blog_tags
        if category is not None:
            blog_category = Category.query.filter_by(name=category).first()
            if blog_category is None:
                blog_category = Category()
                blog_category.name = category
                blog_category.save()
            blog.category = blog_category
        blog.save()
        return 'success'

    @login_required
    def delete(self, blogId):
        if not current_user.is_superuser:
            return 'forbidden'
        blog = Blog.query.filter_by(id=blogId).first()
        if blog is None:
            return 'blog is not exist'
        blog.delete()
        return 'success'


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
