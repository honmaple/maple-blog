#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-13 14:47:19 (CST)
# Last Update:星期二 2016-12-13 15:41:31 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request, current_app, render_template
from flask.views import MethodView
from flask_login import login_required, current_user
from maple.extensions import csrf
from .models import TimeLine


class TimeLineListView(MethodView):
    decorators = [csrf.exempt]

    def get_page_info(self):
        page = request.args.get('page', 1, type=int)
        if hasattr(self, 'per_page'):
            per_page = getattr(self, 'per_page')
            number = request.args.get('number', per_page, type=int)
        else:
            per_page = current_app.config.setdefault('PER_PAGE', 10)
            number = request.args.get('number', per_page, type=int)
        if number > 100:
            number = current_app.config['PER_PAGE']
        return page, number

    def get(self):
        page, number = self.get_page_info()
        filter_dict = {'hide': False}
        timelines = TimeLine.get_list(page, number, filter_dict,
                                      ('-created_at', ))
        return render_template('blog/timeline.html', timelines=timelines)

    @login_required
    def post(self):
        if not current_user.is_superuser:
            return 'Fobidden'
        post_data = request.get_json()
        content = post_data.pop('content', None)
        hide = post_data.pop('hide', None)
        if content is None:
            return 'content is None'
        hide = True if hide == 'True' or hide == '1' else False
        timeline = TimeLine()
        timeline.content = content
        timeline.hide = hide
        timeline.author = current_user
        timeline.save()
        return 'success'
