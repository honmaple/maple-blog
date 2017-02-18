#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-13 14:47:19 (CST)
# Last Update:星期六 2017-2-18 18:13:50 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request
from flask_login import current_user
from common.views import BaseMethodView as MethodView
from common.utils import gen_filter_dict, gen_filter_date, gen_order_by
from common.response import HTTPResponse
from common.serializer import Serializer, PageInfo
from .models import TimeLine


class TimeLineListView(MethodView):
    def get(self):
        query_dict = request.data
        page, number = self.page_info
        keys = ['content']
        equal_key = []
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key,
                                      current_user)
        timelines = TimeLine.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        serializer = Serializer(timelines.items, many=True)
        pageinfo = PageInfo(timelines)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS,
            data=serializer.data,
            pageinfo=pageinfo).to_response()
