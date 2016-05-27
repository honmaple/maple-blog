#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: helpers.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-05-27 18:16:17 (CST)
# Last Update:星期五 2016-5-27 18:17:7 (CST)
#          By:
# Description:
# **************************************************************************
from flask import abort


def is_num(num):
    if num is not None:
        try:
            num = int(num)
            if num > 0:
                return num
            else:
                abort(404)
        except ValueError:
            abort(404)
