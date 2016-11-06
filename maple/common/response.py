#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: response.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-05 15:18:19 (CST)
# Last Update:星期六 2016-11-5 19:12:35 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.response import HTTPResponse as Response
from flask_babelex import gettext as _


class HTTPResponse(Response):
    NORMAL_STATUS = '200'
    USER_EMAIL_WAIT = '301'
    BLOG_ID_NOT_EXIST = '401'

    STATUS_DESCRIPTION = {
        NORMAL_STATUS: 'normal',
        USER_EMAIL_WAIT: _('Your confirm link have not out of time,\
        Please confirm your email in time'),
        BLOG_ID_NOT_EXIST: _('Blog ID should exist')
    }
