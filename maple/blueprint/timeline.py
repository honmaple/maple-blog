#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: timeline.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-02-08 14:45:34 (CST)
# Last Update: Wednesday 2018-11-21 14:01:51 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from flask_maple.views import MethodView
from flask_maple.response import HTTP
from maple.extension import cache
from maple.helper import cache_key
from maple.model import TimeLine


class TimeLineView(MethodView):
    per_page = 10

    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        query_dict = request.data
        page, number = self.pageinfo
        filter_dict = {'is_hidden': False}
        order_by = ('-created_at', )
        timelines = TimeLine.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        if query_dict.pop('from', None) == 'blog':
            return HTTP.HTML('timeline/macro.html', timelines=timelines)
        return HTTP.HTML('timeline/itemlist.html', timelines=timelines)
