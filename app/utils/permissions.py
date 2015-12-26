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
from flask_login import current_user
from flask_principal import Permission, RoleNeed, UserNeed, identity_loaded

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

