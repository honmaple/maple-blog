#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: timeline.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-13 15:41:50 (CST)
# Last Update:星期二 2016-12-13 15:45:13 (CST)
#          By:
# Description:
# **************************************************************************
from .views import BaseModelView
from maple.timeline.models import TimeLine
from maple.extensions import db

__all__ = ['register_timeline']


class TimeLineView(BaseModelView):
    column_editable_list = ['hide', 'author']
    column_filters = ['created_at', 'author']
    form_widget_args = {'content': {'rows': 10}}


def register_timeline(admin):
    admin.add_view(
        TimeLineView(
            TimeLine,
            db.session,
            name='管理时间轴',
            endpoint='admin_timeline',
            category='管理博客'))
