#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: time.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-23 10:35:24
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from functools import wraps
from datetime import datetime,timedelta
from flask import flash, redirect, url_for
from flask.ext.login import current_user

def check_overtime(func):
    '''判断发送的验证邮件是否过期'''
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if datetime.now() < current_user.send_email_time + \
                timedelta(seconds=360):
            flash("你获取的验证链接还未过期，请尽快验证")
            return redirect(url_for('index.logined_user',
                                    name=current_user.name))
        return func(*args, **kwargs)

    return decorated_function
