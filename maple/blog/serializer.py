#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: serializer.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-12 10:19:56 (CST)
# Last Update: Monday 2019-09-09 00:45:31 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_maple.serializer import Serializer


class ArticleSerializer(Serializer):
    class Meta:
        exclude = ["user", "user_id"]
        extra = ["htmlcontent"]
