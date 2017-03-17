#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-13 14:47:19 (CST)
# Last Update:星期五 2017-3-17 23:25:41 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request, render_template
from flask_login import login_required, current_user
from maple.extensions import csrf
from maple.common.views import BaseMethodView as MethodView
from .models import TimeLine


class TimeLineListView(MethodView):
    decorators = [csrf.exempt]

    def get(self):
        page, number = self.page_info
        filter_dict = {'hide': False}
        order_by = ('created_at', )
        timelines = TimeLine.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
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
