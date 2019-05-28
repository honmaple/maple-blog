#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: config.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 16:49:50 (CST)
# Last Update: Friday 2019-06-07 03:27:11 (CST)
#          By:
# Description:
# ********************************************************************************
import os

CORS = {
    r"/*": {
        "origins": [r'^https://.+honmaple.com$', r"https://honmaple.me"]
    }
}
# SUBDOMAIN = "static.honmaple.com"
SUBDOMAIN = None
UPLOAD_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        os.path.pardir,
        'storage',
    ))
UPLOAD_ALLOWED_EXTENSIONS = ["js", "css", "png", "jpg"]
