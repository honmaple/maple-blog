#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: article.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-12 10:18:31 (CST)
# Last Update: Monday 2019-09-23 17:06:31 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from flask_maple.response import HTTP
from maple.assertion import assert_request
from maple.blog.assertion import ArticleAssert
from maple.blog.db import Article
from maple.blog.serializer import ArticleSerializer
from maple.utils import filter_maybe, AuthMethodView


class ArticleAPI(AuthMethodView):
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
        serializer = ArticleSerializer(ins)
        return HTTP.OK(data=serializer.data)

    @assert_request(ArticleAssert)
    def post(self):
        data = request.data
        user = request.user

        ins = Article(
            title=data["title"],
            content=data["content"],
            user_id=user.id,
        )
        ins.save()
        serializer = ArticleSerializer(ins)
        return HTTP.OK(data=serializer.data)
