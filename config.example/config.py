#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: config_example.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-10-25 08:01:06
# *************************************************************************
from datetime import timedelta

DEBUG = False
SECRET_KEY = 'secret key'
SECRET_KEY_SALT = 'you will never guess'

# remember me to save cookies
PERMANENT_SESSION_LIFETIME = timedelta(days=3)
REMEMBER_COOKIE_DURATION = timedelta(days=3)
ONLINE_LAST_MINUTES = 5

# You want show how many topics per page
PER_PAGE = 12

# This will show at html footer
AUTHOR_NAME = 'Copyright © 2015-2016 honmaple. All rights reserved.'
ADMIN_URL = '/admin/aa'

# redis
REDIS = {'db': 0, 'password': 'ss'}

# Use cache
CACHE_TYPE = 'redis'
CACHE_DEFAULT_TIMEOUT = 60
CACHE_KEY_PREFIX = 'cache:'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = '6379'
CACHE_REDIS_PASSWORD = 'redis password'
CACHE_REDIS_DB = 1

MIDDLEWARE = [
    'maple.common.middleware.CommonMiddleware',
    # 'flask_maple.permission.middleware.PermissionMiddleware'
]

# Mail such as qq
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'Your domain email'
MAIL_PASSWORD = 'Your password'
MAIL_DEFAULT_SENDER = 'Your domain email'

# Log,if SEND_LOGS is True when web app has some error happen(500)
# the email will be sent to RECEIVER
SEND_LOGS = False
RECEIVER = ["yourname@gmail.com"]
INFO_LOG = "info.log"
ERROR_LOG = "error.log"

# Sql
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/db_name'
# SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'

# Locale
LANGUAGES = {'en': 'English', 'zh': 'Chinese'}
