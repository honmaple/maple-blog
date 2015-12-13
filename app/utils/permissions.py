#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: permissions.py
#   Author:JiangLin 
#   Mail:xiyang0807@gmail.com 
#   Created Time: 2015-12-12 20:28:00
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# from ..models import User
# from flask import g
from functools import wraps
from flask import flash,redirect,url_for
from flask_login import current_user

class Permission(object):
    def __init__(self, permission):
        self.user = current_user
        self.permission = permission

    def __call__(self, func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            self.confirm_permission(self.permission)
            return func(*args, **kwargs)
        return decorated_function

    def confirm_permission(self,permission):
        if permission == 'admin':
            if not self.user.admin:
                print(self.user.admin)
                flash("你没有超级管理员权限进行操作")
                return redirect(url_for('index.index'))
