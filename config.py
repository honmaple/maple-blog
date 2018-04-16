#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: config.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-14 19:34:19 (CST)
# Last Update: Saturday 2018-03-17 18:00:41 (CST)
#          By:
# Description:
# **************************************************************************
from datetime import timedelta
import os

PATH = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SECRET_KEY = 'asdadasd'
SECRET_KEY_SALT = 'asdasdads'
TEMPLATES_AUTO_RELOAD = True

AUTHOR_NAME = '© 2015-2018 honmaple. All rights reserved.'
PERMANENT_SESSION_LIFETIME = timedelta(days=3)
REMEMBER_COOKIE_DURATION = timedelta(days=3)

# WTF_CSRF_CHECK_DEFAULT = False
ONLINE_LAST_MINUTES = 5

PER_PAGE = 6

SERVER_NAME = '127.0.0.1:8001'
SESSION_COOKIE_DOMAIN = "127.0.0.1:8001"
REDIS = {'db': 0, 'password': 'redis'}


# 定制缓存 = 60
CACHE_TYPE = 'null'
CACHE_DEFAULT_TIMEOUT = 60
CACHE_KEY_PREFIX = 'cache:'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = '6379'
CACHE_REDIS_PASSWORD = 'redis'
CACHE_REDIS_DB = 0
CACHE_NO_NULL_WARNING = True

MIDDLEWARE = ['maple.middleware.Middleware', ]

MAIL_SERVER = ""
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = ""
MAIL_PASSWORD = "as"
MAIL_DEFAULT_SENDER = ''

ADMIN_URL = '/admin'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/blog'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'

BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'
BABEL_TRANSLATION_DIRECTORIES = os.path.join(PATH, 'LANG')

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
