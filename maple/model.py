#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: model.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2017-08-24 15:13:33 (CST)
# Last Update: Monday 2019-07-01 20:00:58 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.auth.models import GroupMixin, UserMixin
from flask_maple.models.permission import PermissionMixin
from maple.extension import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    @property
    def is_admin(self):
        return self.is_authenticated and self.is_superuser

    @property
    def token(self):
        return self.email_token

    @classmethod
    def check_token(cls, token, max_age=24 * 3600 * 30):
        return cls.check_email_token(token, max_age)


class Group(db.Model, GroupMixin):
    __tablename__ = 'group'


class Permission(db.Model, PermissionMixin):
    __tablename__ = 'permission'
