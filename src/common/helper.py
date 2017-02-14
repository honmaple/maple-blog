#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: helper.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-01-08 20:33:31 (CST)
# Last Update:星期四 2017-1-12 16:7:24 (CST)
#          By:
# Description:
# **************************************************************************
from flask import current_app
from random import sample
from string import ascii_letters, digits


def random_string(num):
    if num > 64:
        num = 20
    return ''.join(sample(ascii_letters + digits, num))


class Config(object):
    def __getattr__(self, name):
        return getattr(current_app.config, name)

    def __getitem__(self, name):
        return current_app.config[name]

    def __setitem__(self, name, value):
        current_app.config[name] = value

    def __delitem__(self, name):
        del current_app.config[name]


config = Config()
