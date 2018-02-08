#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: config.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-14 19:34:19 (CST)
# Last Update: 星期五 2018-02-09 16:54:47 (CST)
#          By:
# Description:
# **************************************************************************
from datetime import timedelta

TEMPLATES_AUTO_RELOAD = True
DEBUG = False
SECRET_KEY = 'asdadasd'
SECRET_KEY_SALT = 'asdasdads'

AUTHOR_NAME = 'Copyright © 2015-2016 honmaple. All rights reserved.'
PERMANENT_SESSION_LIFETIME = timedelta(days=3)
REMEMBER_COOKIE_DURATION = timedelta(days=3)

ONLINE_LAST_MINUTES = 5

PER_PAGE = 6

# SERVER_NAME = 'localhost:5000'
REDIS = {'db': 0, 'password': 'redis'}

# 定制缓存 = 60
CACHE_TYPE = 'null'
CACHE_DEFAULT_TIMEOUT = 60
CACHE_KEY_PREFIX = 'cache:'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = '6379'
CACHE_REDIS_PASSWORD = 'redis'
CACHE_REDIS_DB = 0

BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'

MIDDLEWARE = [
    'maple.middleware.Middleware',
]

MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "admin@honmaple.com"
MAIL_PASSWORD = "as"
MAIL_DEFAULT_SENDER = 'admin@honmaple.com'

SEND_LOGS = True
RECEIVER = ["xiyang0807@gmail.com"]

ADMIN_URL = '/admin'

SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/blog'
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'

LOGGING = {
    'info': 'logs/info.log',
    'error': 'logs/error.log',
    'send_mail': False,
    'toaddrs': [],
    'subject': 'Your Application Failed',
    'formatter': '''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s

            Message:

            %(message)s
            '''
}
