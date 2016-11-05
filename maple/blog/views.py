#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
# *************************************************************************
from flask import (request, redirect, url_for, flash)
from flask.views import MethodView
from flask_login import current_user, login_required
from flask_maple.views import ViewList, View
from maple.extensions import redis_data
from maple.blog.forms import CommentForm
from maple.user.models import User
from maple.main.permissions import writer_permission
from .models import Blog, Comment, Category
from flask_babelex import gettext as _
from urllib.parse import urljoin
from maple.filters import safe_markdown
from werkzeug.contrib.atom import AtomFeed
from werkzeug.utils import escape
from maple.common.response import HTTPResponse
from .serializer import BlogSerializer, CommentSerializer


class BlogListView(ViewList):
    model = Blog
    serializer = BlogSerializer
    template = 'blog/bloglist.html'

    def get_filter_dict(self):
        category = request.args.get('category')
        tag = request.args.get('tag')
        author = request.args.get('author')
        filter_dict = {}
        if category is not None:
            category = Category.query.filter_by(name=category).first_or_404()
            filter_dict.update(category=category)
        if tag is not None:
            filter_dict.update(tag=tag)
        if author is not None:
            author = User.query.filter_by(username=author).first_or_404()
            filter_dict.update(author=author)
        return filter_dict


class BlogView(View):
    model = Blog
    serializer = BlogSerializer
    template = 'blog/blog.html'

    def get(self, blogId):
        '''记录用户浏览次数'''
        redis_data.zincrby('visited:article', 'article:%s' % str(blogId), 1)
        return super(BlogView, self).get(blogId)


class CommentListView(ViewList):
    form = CommentForm
    model = Comment
    serializer = CommentSerializer
    template = 'blog/commentlist.html'
    per_page = 100

    def get_filter_dict(self):
        filter_dict = {}
        blog_id = request.args.get('blogId', type=int)
        if blog_id is None:
            return HTTPResponse(HTTPResponse.BLOG_ID_NOT_EXIST).to_response()
        filter_dict.update(blog_id=blog_id)
        return filter_dict

    def get_render_info(self, data):
        data.update(form=self.form())
        return data

    @login_required
    def post(self):
        blog_id = request.args.get('blogId', type=int)
        form = self.form()
        if not writer_permission.can():
            flash(_('You have not confirm your account'))
            return redirect(url_for('blog.blog', blogId=blog_id))
        if form.validate_on_submit():
            if Blog.query.filter_by(id=blog_id).first() is None:
                return HTTPResponse(
                    HTTPResponse.BLOG_ID_NOT_EXIST).to_response()
            comment = Comment()
            comment.author = current_user
            comment.content = form.content.data
            comment.blog_id = blog_id
            comment.add()
            return redirect(
                url_for(
                    'blog.blog', blogId=blog_id, _anchor='blog-comment'))
        return redirect(
            url_for(
                'blog.blog', blogId=blog_id, _anchor='blog-comment'))


class BlogArchiveView(ViewList):
    per_page = 30
    model = Blog
    serializer = BlogSerializer
    template = 'blog/archives.html'


class BlogRssView(MethodView):
    def get(self):
        feed = AtomFeed(
            'HoMaple的个人博客',
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
