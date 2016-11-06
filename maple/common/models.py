#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: models.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-05 15:25:44 (CST)
# Last Update:星期六 2016-11-5 15:28:5 (CST)
#          By:
# Description:
# **************************************************************************
from maple.extensions import db


class BaseModel(object):
    def save(self):
        db.session.commit()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
