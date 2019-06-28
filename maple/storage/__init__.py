#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:40 (CST)
# Last Update: Sunday 2019-06-30 14:15:42 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import Blueprint

from maple.extension import csrf

from . import config
from .router import (BucketListView, BucketView, FileListView, FileShowView,
                     FileView)

site = Blueprint('storage', __name__)

site.add_url_rule(
    '/api/bucket',
    view_func=BucketListView.as_view('buckets'),
)
site.add_url_rule(
    '/api/bucket/<int:pk>',
    view_func=BucketView.as_view('bucket'),
)
site.add_url_rule(
    '/api/file/<bucket>',
    view_func=FileListView.as_view('files'),
)
site.add_url_rule(
    '/api/file/<bucket>/<int:pk>',
    view_func=FileView.as_view('file'),
)

show = FileShowView.as_view("show")

site.add_url_rule(
    "/",
    defaults={"filename": "index.html"},
    view_func=show,
)
site.add_url_rule(
    "/<path:filename>",
    view_func=show,
)


def init_conf(app):
    variables = [item for item in dir(config) if not item.startswith("__")]
    for k, v in app.config.get("STORAGE", dict()).items():
        if k not in variables:
            continue
        setattr(config, k, v)


def init_app(app):
    init_conf(app)
    app.register_blueprint(site, subdomain=config.SUBDOMAIN)
    csrf.exempt(site)
