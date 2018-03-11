#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: timeline.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2018-03-11 20:51:54 (CST)
# Last Update: Sunday 2018-03-11 21:42:21 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import jsonify
from flask_maple.views import MethodView
from flask_maple.serializer import Serializer

from maple.model import TimeLine


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
        return jsonify(status=200, data=serializer.data)
