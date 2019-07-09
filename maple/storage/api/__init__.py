#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-03 21:39:52 (CST)
# Last Update: Wednesday 2019-07-10 00:22:32 (CST)
#          By:
# Description:
# ********************************************************************************
from .bucket import BucketListView, BucketView
from .file import FileListView
from .filepath import FilePathListView


def init_api(app):
    app.add_url_rule(
        '/api/bucket',
        view_func=BucketListView.as_view('buckets'),
    )
    app.add_url_rule(
        '/api/bucket/<int:pk>',
        view_func=BucketView.as_view('bucket'),
    )

    files = FileListView.as_view('files')
    app.add_url_rule(
        "/api/file",
        defaults={"bucket": "default"},
        view_func=files,
    )
    app.add_url_rule(
        '/api/file/<bucket>',
        view_func=files,
    )

    filepaths = FilePathListView.as_view('filepaths')
    app.add_url_rule(
        '/api/filepath',
        defaults={"bucket": "default"},
        view_func=filepaths,
    )
    app.add_url_rule(
        '/api/filepath/<bucket>',
        view_func=filepaths,
    )
