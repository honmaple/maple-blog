#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: timeline.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 22:49:44 (CST)
# Last Update: Friday 2019-05-24 22:56:43 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_maple.response import HTTP
from flask_maple.serializer import Serializer
from flask_maple.views import MethodView

from maple.blog.db import TimeLine


class TimeLineAPI(MethodView):
    def get(self):
        page, number = self.pageinfo
        filter_dict = {'is_hidden': False}
        order_by = ('-created_at', )
        timelines = TimeLine.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        serializer = Serializer(
            timelines,
            exclude=['user', 'user_id', 'is_hidden'],
            extra=['datetime_format'])
        return HTTP.OK(data=serializer.data)
