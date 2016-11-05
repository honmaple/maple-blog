#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: serializer.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-05 16:21:53 (CST)
# Last Update:星期六 2016-11-5 16:24:58 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.serializer import Serializer
from .models import User


class UserSerializer(Serializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'roles', 'is_confirmed', 'is_superuser',
                  'registered_time', 'confirmed_time', 'introduce', 'school']
