#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: permissions.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-12 20:28:00
# *************************************************************************
from maple import app
from flask_login import current_user
from flask_principal import Permission, RoleNeed, UserNeed, identity_loaded
from flask import abort, jsonify
from functools import wraps
from flask import g, redirect, flash, url_for
from maple import redis_data
from time import time
from flask import request
from collections import namedtuple
from functools import partial

Need = namedtuple('need', ['method', 'value'])
EditQuestionNeed = partial(Need, 'id')
PostNeed = partial(Need, 'post')
GroupNeed = partial(Need, 'id')
BoardNeed = partial(Need, 'id')
UserNameNeed = partial(Need, 'name')
ShowNeed = partial(Need, 'permission')


class MyPermission(object):
    def __init__(self, required=None, name=None):
        self.required = required

    def __call__(self, func):
        @wraps(func)
        def decorator(*args, **kwargs):
            if not self.allow():
                return self.action()
            return func(*args, **kwargs)

        return decorator

    def allow(self):
        return False

    def action(self):
        abort(403)


class OwnPermission(MyPermission):
    def allow(self):
        if current_user.name == g.user_url:
            return True
        else:
            return False

    def action(self):
        return redirect(url_for('user.setting', user_url=current_user.name))


class GuestPermission(MyPermission):
    def allow(self):
        if not g.user.is_authenticated:
            return True
        else:
            return False

    def action(self):
        flash('你已经登陆,不能重复登陆')
        return redirect(url_for('forums.forums'))


class TimePermission(MyPermission):
    def allow(self):
        user = 'user:%s' % str(current_user.id)
        last_time = redis_data.hget(user, 'send_email_time')
        now_time = int(time()) + 28800
        if last_time is None:
            last_time = now_time
            return True
        else:
            last_time = int(last_time)
        if last_time < now_time - 3600:
            return True
        else:
            return False

    def action(self):
        error = u'你的验证链接还未过期，请尽快验证'
        return error


own_permission = OwnPermission()
guest_permission = GuestPermission()
time_permission = TimePermission()

super_permission = Permission(RoleNeed('super'))
admin_permission = Permission(RoleNeed('admin')).union(super_permission)
member_permission = Permission(RoleNeed('member')).union(admin_permission)
banned_permission = Permission(RoleNeed('banned')).union(member_permission)
confirm_permission = Permission(RoleNeed('confirm')).union(member_permission)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        identity.provides.add(RoleNeed(current_user.roles))

    if hasattr(current_user, 'is_superuser'):
        if current_user.is_superuser:
            identity.provides.add(RoleNeed('super'))

    #  if hasattr(current_user, 'is_confirmed'):
    #  if current_user.is_confirmed:
    #  identity.provides.add(PostNeed(True))

    #  if hasattr(current_user, 'questions'):
    #  for question in current_user.questions:
    #  identity.provides.add(EditQuestionNeed(int(question.id)))

    #  if hasattr(current_user, 'infor'):
    #  score = current_user.infor.score
    #  if score > 5:
    #  identity.provides.add(PostNeed(score))
    #  elif score > 1:
    #  identity.provides.add(PostNeed(score))
    #  else:
    #  pass

    #  if hasattr(current_user, 'groups'):
    #  for group in current_user.groups:
    #  identity.provides.add(GroupNeed(int(group.id)))

    #  if hasattr(Group, 'permission'):
    #  identity.provides.add(ShowNeed(identity.group.permission))
    #  print(identity)

    #  identity.provides.add(ShowNeed(1))
    #  identity.provides.add(ShowNeed(2))
    #  identity.provides.add(ShowNeed(3))
    #  print('%s\n'%identity)

    # if hasattr(current_user, 'name'):
    #     identity.provides.add(UserNameNeed(current_user.name))
    # identity.allow_admin = admin_permission.allows(identity)
    # identity.allow_edit = editor_permission.allows(identity)
    # identity.allow_write = writer_permission.allows(identity)
