#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: response.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-25 11:21:35 (CST)
# Last Update:星期四 2017-2-2 21:25:7 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.response import HTTPResponse as Response


class HTTPResponse(Response):

    AUTH_USER_OR_PASSWORD_ERROR = '600'
    AUTH_USERNAME_UNIQUE = '601'
    AUTH_EMAIL_UNIQUE = '602'

    HTTP_CLOUD_NOT_EXIST = '404'
    # 项目
    HTTP_CLOUD_PROJECT_NOT_EXIST = '701'

    HTTP_CLOUD_PARA_ERROR = '401'

    OTHER_ERROR = '900001'

    Response.STATUS_DESCRIPTION.update({
        AUTH_USER_OR_PASSWORD_ERROR: 'username or password error',
        AUTH_USERNAME_UNIQUE: '用户名已注册',
        AUTH_EMAIL_UNIQUE: '邮箱已注册',
        HTTP_CLOUD_NOT_EXIST: '404',
        HTTP_CLOUD_PARA_ERROR: '参数错误',
        HTTP_CLOUD_PROJECT_NOT_EXIST: '项目不存在',
        OTHER_ERROR: '其它错误'
    })
