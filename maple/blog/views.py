#!/usr/bin/env python
# -*- coding=UTF-8 -*-
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
from maple import db, redis_data, cache
from maple.blog.forms import CommentForm
from maple.main.permissions import writer_permission
from .models import Blog, Comment, Category
from flask_babelex import gettext as _
from urllib.parse import urljoin
from maple.filters import safe_markdown
from werkzeug.contrib.atom import AtomFeed
from werkzeug.utils import escape


def make_external(url):
    return urljoin(request.url_root, url)


class BlogListView(MethodView):
    def get_request_info(self):
        page = request.args.get('page', 1, type=int)
        category = request.args.get('category')
        tag = request.args.get('tag')
        filter_dict = {}
        if category is not None:
            category = Category.query.filter_by(name=category).first_or_404()
            filter_dict.update(category=category)
        if tag is not None:
            filter_dict.update(tag=tag)
        return page, filter_dict

    @cache.cached(timeout=180)
    def get(self):
        page, filter_dict = self.get_request_info()
        blogs = Blog.get_blog_list(page, filter_dict)
        data = {'blogs': blogs}
        return render_template('blog/bloglist.html', **data)


class BlogView(MethodView):
    @cache.cached(timeout=30)
    def get(self, blogId):
        '''记录用户浏览次数'''
        redis_data.zincrby('visited:article', 'article:%s' % str(id), 1)
        blog = Blog.get(blogId)
        tags = Blog.tags
        data = {'blog': blog, 'tags': tags}
        return render_template('blog/blog.html', **data)


class CommentListView(MethodView):
    # form = CommentForm()

    def __init__(self):
        super(MethodView, self).__init__()
        self.form = CommentForm()

    def get(self, blogId):
        page = request.args.get('page', 1, type=int)
        filter_dict = {}
        filter_dict.update(blog_id=blogId)
        comments = Comment.get_comment_list(page, filter_dict)
        data = {'comments': comments, 'form': self.form}
        return render_template('blog/commentlist.html', **data)

    @login_required
    def post(self, blogId):
        if not writer_permission.can():
            flash(_('You have not confirm your account'))
            return redirect(url_for('blog.index_num'))
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


class BlogArchiveView(MethodView):
    def get(self):
        page = request.args.get('page', 1, type=int)
        blogs = Blog.query.paginate(page, 30, True)
        data = {'blogs': blogs}
        return render_template('blog/archives.html', **data)


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
                     url=make_external(url_for(
                         'blog.blog', blogId=blog.id)),
                     updated=blog.created_at
                     if blog.updated_at is not None else blog.created_at,
                     published=blog.created_at)
        return feed.get_response()
