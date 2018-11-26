#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: index.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-02-08 14:45:03 (CST)
# Last Update: Wednesday 2018-11-21 14:05:45 (CST)
#          By:
# Description:
# ********************************************************************************
from flask.views import MethodView
from flask_maple.response import HTTP
from maple.extension import cache


class IndexView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return HTTP.HTML("index/index.html")


class AboutView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return HTTP.HTML("index/about.html")


class FriendView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return HTTP.HTML("index/friends.html")
