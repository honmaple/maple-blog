#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: permissions.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-12 20:28:00
# *************************************************************************
from flask_principal import Permission, RoleNeed

super_permission = Permission(RoleNeed('Super'))
admin_permission = Permission(RoleNeed('Admin')).union(super_permission)
writer_permission = Permission(RoleNeed('Writer')).union(admin_permission)
visitor_permission = Permission(RoleNeed('Visitor')).union(writer_permission)
