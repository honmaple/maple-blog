#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: serializer.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-05 19:31:57 (CST)
# Last Update:星期六 2016-11-5 19:33:25 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.serializer import Serializer
from .models import Books


class BookSerializer(Serializer):
    class Meta:
        model = Books
        fields = ['id', 'tag', 'name', 'author', 'content']
