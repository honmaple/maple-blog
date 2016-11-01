#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: development.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-08-08 16:13:42 (CST)
# Last Update:星期三 2016-10-5 15:16:5 (CST)
#          By:
# Description:
# **************************************************************************
from datetime import timedelta

DEBUG = True
SECRET_KEY = 'secret key'
SECURITY_PASSWORD_SALT = 'you will never guess'

# remember me to save cookies
PERMANENT_SESSION_LIFETIME = timedelta(days=3)
REMEMBER_COOKIE_DURATION = timedelta(days=3)
ONLINE_LAST_MINUTES = 5

# You want show how many topics per page
PER_PAGE = 12

# This will show at html footer
AUTHOR_NAME = 'Copyright © 2015-2016 honmaple. All rights reserved.'

# Use cache
CACHE_TYPE = 'redis'
CACHE_DEFAULT_TIMEOUT = 60
CACHE_KEY_PREFIX = 'cache:'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = '6379'
CACHE_REDIS_PASSWORD = 'redis password'
CACHE_REDIS_DB = 1


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
