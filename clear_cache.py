#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: clear_cache.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-15 22:37:36 (CST)
# Last Update:星期六 2016-11-5 21:55:14 (CST)
#          By:
# Description:
# **************************************************************************
from flask_cache import Cache
from maple import create_app

app = create_app()


def register_cache(app):
    cache = Cache(config={'CACHE_TYPE': 'redis'})
    return cache


cache = register_cache(app)


def main():
    cache.init_app(app)
    with app.app_context():
        cache.clear()


if __name__ == '__main__':
    main()
