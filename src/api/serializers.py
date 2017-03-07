#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: serializers.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-07 14:14:44 (CST)
# Last Update:星期二 2017-3-7 19:44:39 (CST)
#          By:
# Description:
# **************************************************************************
from common.serializer import Serializer, PageInfo


class BlogSerializer(Serializer):
    class Meta:
        include = ['id', 'title', 'created_at', 'author', 'tags', 'category',
                   'content']


class BlogCategorySerializer(Serializer):
    class Meta:
        include = ['id', 'name']
