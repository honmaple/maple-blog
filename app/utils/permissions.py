#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: permissions.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-12 20:28:00
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from app import app
from app import redis_data
from flask_login import current_user
from flask_principal import Permission, RoleNeed, UserNeed, identity_loaded
# from functools import wraps
from flask import abort

super_permission = Permission(RoleNeed('super'))
admin_permission = Permission(RoleNeed('admin')).union(super_permission)
editor_permission = Permission(RoleNeed('editor')).union(admin_permission)
writer_permission = Permission(RoleNeed('writer')).union(editor_permission)
visitor_permission = Permission(RoleNeed('visitor')).union(writer_permission)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        identity.provides.add(RoleNeed(current_user.roles))

    if hasattr(current_user, 'is_superuser') and current_user.is_superuser:
        identity.provides.add(RoleNeed('super'))

    if hasattr(current_user, 'is_confirmed') and current_user.is_confirmed:
        identity.provides.add(RoleNeed('writer'))

    # if hasattr(current_user, 'name'):
        # identity.provides.add(RoleNeed(current_user.name))
    # identity.allow_admin = admin_permission.allows(identity)
    # identity.allow_edit = editor_permission.allows(identity)
    # identity.allow_write = writer_permission.allows(identity)


def set_blacklist(user_ip):
    '''设置黑名单'''
    redis_data.sadd('users:blacklist', user_ip)


def set_writelist(user_ip):
    '''设置白名单'''
    redis_data.sadd('users:writelist', user_ip)


def allow_ip(user_ip):
    visited_users = redis_data.smembers('users:blacklist')
    if user_ip.encode() in visited_users:
        abort(501)
    else:
        pass

# def allow_ip(user_ip):
    # def decorator(f):
        # @wraps(f)
        # def decorated_function(*args, **kwargs):
        # '''查询IP是否在黑名单中'''
        # visited_users = redis_data.smembers('blacklist')
        # if user_ip in visited_users:
        # abort(404)
        # else:
        # pass
        # return decorated_function
    # return decorator
