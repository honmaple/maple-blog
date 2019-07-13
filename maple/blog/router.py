#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: router.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 18:43:30 (CST)
# Last Update: Thursday 2019-07-11 18:06:49 (CST)
#          By:
# Description:
# ********************************************************************************
from collections import OrderedDict
from urllib.parse import urljoin

from flask import request, url_for
from flask_maple.response import HTTP
from maple.default import SITE
from maple.utils import MethodView, filter_maybe
from werkzeug.contrib.atom import AtomFeed

from .db import Article, TimeLine


class ArticleListView(MethodView):
    per_page = 10

    def get(self):
        data = request.data
        page, number = self.pageinfo
        params = filter_maybe(
            data, {
                "tag": "tags__name",
                "category": "category__name",
                "title": "title__contains",
                "year": "created_at__year",
                "month": "created_at__month"
            })
        order_by = ("-created_at", )

        ins = Article.query.filter_by(**params).order_by(*order_by).paginate(
            page, number)
        return HTTP.HTML('articles.html', articles=ins)


class ArticleView(MethodView):
    def get(self, pk):
        ins = Article.query.filter_by(id=pk).first_or_404()
        '''记录用户浏览次数'''
        ins.read_times = 1
        data = {'article': ins}
        return HTTP.HTML('article.html', **data)


class ArchiveView(MethodView):
    def get(self, year=None, month=None):
        data = request.data
        params = filter_maybe(
            data, {
                "tag": "tags__name",
                "category": "category__name",
                "title": "title__contains",
                "year": "created_at__year",
                "month": "created_at__month"
            })
        if year:
            params.update(created_at__year=year)
        if month:
            params.update(created_at__month=month)
        order_by = ("-created_at", )
        ins = OrderedDict()
        for article in Article.query.filter_by(**params).order_by(*order_by):
            date = article.created_at.strftime("%Y年%m月")
            ins.setdefault(date, [])
            ins[date].append(article)
        return HTTP.HTML('archives.html', articles=ins)


class ArticleRssView(MethodView):
    def get(self):
        title = SITE['title']
        subtitle = SITE['subtitle']
        feed = AtomFeed(
            '%s' % (title),
            feed_url=request.url,
            url=request.url_root,
            subtitle=subtitle)
        articles = Article.query.limit(10)
        for article in articles:
            feed.add(
                article.title,
                article.to_html(),
                content_type='html',
                author=article.user.username,
                url=urljoin(request.url_root,
                            url_for('blog.article', pk=article.id)),
                updated=article.updated_at,
                published=article.created_at)
        return feed.get_response()


class TimeLineView(MethodView):
    def get(self):
        page, number = self.pageinfo
        params = {'is_hidden': False}
        order_by = ('-created_at', )
        timelines = TimeLine.query.filter_by(
            **params).order_by(*order_by).paginate(page, number)
        return HTTP.HTML('timelines.html', timelines=timelines)
