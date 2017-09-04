#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-13 14:47:19 (CST)
# Last Update:星期一 2017-9-4 11:14:43 (CST)
#          By:
# Description:
# **************************************************************************
from flask import jsonify, render_template, request
from flask_login import login_required

from maple.common.validator import Validator
from maple.common.views import BaseMethodView as MethodView
from maple.extensions import cache, csrf
from maple.helper import cache_key
from maple.utils import superuser_required

from .models import TimeLine


class TimeLineListView(MethodView):
    per_page = 10
    decorators = [csrf.exempt]

    @cache.cached(timeout=180, key_prefix=cache_key)
    def get(self):
        query_dict = request.data
        page, number = self.page_info
        filter_dict = {'hide': False}
        order_by = ('-created_at', )
        timelines = TimeLine.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        if query_dict.pop('from', None) == 'blog':
            return render_template('timeline/_macro.html', timelines=timelines)
        return render_template('timeline/timeline.html', timelines=timelines)

    @superuser_required
    def post(self):
        author = request.user
        validator = Validator('timeline')
        validator.add_validator('content', type=str, required=True)
        post_data = request.data
        v = validator.is_valid(post_data)
        if v is not True:
            return jsonify(status=401, message=v)
        content = post_data.pop('content', None)
        hide = post_data.pop('hide', None)
        hide = True if hide in ['true', 'True', '1', True] else False
        timeline = TimeLine(content=content, hide=hide, author=author)
        timeline.save()
        return jsonify(status='200', message=timeline.to_json())
