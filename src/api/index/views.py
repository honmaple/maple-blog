#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: index.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 02:21:04
# *************************************************************************
from flask import (render_template, redirect, url_for, make_response)
from flask.views import MethodView
from maple.extensions import cache
from common.serializer import Serializer
from api.blog.models import Blog
from api.question.models import Question
from .models import Notice


class IndexView(MethodView):
    def get(self):
        blog_key = 'bloglist:index'
        que_key = 'quelist:index'
        notice_key = 'noticelist:index'
        blogs = cache.get(blog_key)
        questions = cache.get(que_key)
        notice = cache.get(que_key)
        if not blogs:
            blogs = Blog.query.paginate(1, 7)
            serializer = Serializer(blogs.items, many=True)
            data = serializer.data
            if data:
                cache.set(blog_key, data, 600)
        if not questions:
            questions = Question.query.filter_by(
                is_private=False).paginate(1, 7)
            serializer = Serializer(questions.items, many=True)
            data = serializer.data
            if data:
                cache.set(que_key, data, 600)
        if not notice:
            notice = Notice.query.first()
            serializer = Serializer(notice)
            data = serializer.data
            if data:
                cache.set(notice_key, data, 600)
        data = {
            'blogs': blogs.items,
            'questions': questions.items,
            'notice': notice,
        }
        return render_template('index/index.html', **data)


class RainView(MethodView):
    def get(self):
        response = make_response(redirect(url_for('index.index')))
        response.delete_cookie('welcome')
        return response


class AboutView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/about.html')


class ResumeView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/resume.html')


class FriendView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/friends.html')
