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

super_permission = Permission(RoleNeed('Super'))
admin_permission = Permission(RoleNeed('Admin')).union(super_permission)
writer_permission = Permission(RoleNeed('Writer')).union(admin_permission)
visitor_permission = Permission(RoleNeed('Visitor')).union(writer_permission)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        identity.provides.add(RoleNeed(current_user.roles))

    if hasattr(current_user, 'is_superuser'):
        if current_user.is_superuser:
            identity.provides.add(RoleNeed('Super'))

    if hasattr(current_user, 'is_confirmed'):
        if current_user.is_confirmed:
            identity.provides.add(RoleNeed('Writer'))

    if hasattr(current_user, 'is_authenticated'):
        if not current_user.is_authenticated:
            identity.provides.add(RoleNeed('Guest'))
