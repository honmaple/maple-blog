#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: config.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 16:49:50 (CST)
# Last Update: Sunday 2019-06-09 17:49:39 (CST)
#          By:
# Description:
# ********************************************************************************
import os

CORS = {
    r"/*": {
        "origins": [r'^https://.+honmaple.com$', r"https://honmaple.me"]
    }
}
HTTPS = True
SUBDOMAIN = None
UPLOAD_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        os.path.pardir,
        'storage',
    ))

UPLOAD_ALLOWED_EXTENSIONS = [
    "ico",
    "txt",
    "html",
    "js",
    "css",
    "png",
    "jpg",
    # "woff2",  # fonts
    # "woff",
    # "ttf",
    # "otf",
    # "eot",
    # "svg",
]

ALLOWED_REFERER = [
    "honmaple.com",
    "*.honmaple.com",
    "honmaple.me",
    "honmaple.org",
    "*.honmaple.org",
    "jianglin.me",
    "localhost",
    "*.localhost",
    "127.0.0.1",
]
