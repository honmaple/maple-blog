#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: clear_cache.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-15 22:37:36 (CST)
# Last Update:星期日 2017-4-2 0:0:11 (CST)
#          By:
# Description:
# **************************************************************************
from flask_cache import Cache
from forums import create_app

app = create_app('config')


def register_cache(app):
    cache = Cache()
    return cache


cache = register_cache(app)


def main():
    cache.init_app(app)
    with app.app_context():
        cache.clear()


if __name__ == '__main__':
    main()
