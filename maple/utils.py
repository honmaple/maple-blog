#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: utils.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-02-08 15:04:16 (CST)
# Last Update: Sunday 2018-11-25 13:43:31 (CST)
#          By:
# Description:
# ********************************************************************************
from datetime import datetime, timedelta


def gen_order_by(query_dict=dict(), keys=[], date_key=True):
    keys.append('id')
    if date_key:
        keys += ['created_at', 'updated_at']
    order_by = ['id']
    descent = query_dict.pop('descent', None)
    if descent is not None:
        descent = descent.split(',')
        descent = list(set(keys) & set(descent))
        order_by = ['-%s' % i for i in descent]
    return tuple(order_by)


def update_maybe(ins, request_data, columns):
    for column in columns:
        value = request_data.get(column)
        if value:
            setattr(ins, column, value)
    return ins


def filter_maybe(request_data, columns, params=None):
    if params is None:
        params = dict()
    is_dict = isinstance(columns, dict)
    for column in columns:
        value = request_data.get(column)
        if not value:
            continue
        key = column if not is_dict else columns.get(column, column)

        if key in ["created_at__gte", "created_at__lte"]:
            value = datetime.strptime(value, '%Y-%m-%d')
        params.update({key: value})
    return params
