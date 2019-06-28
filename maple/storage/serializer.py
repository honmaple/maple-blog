#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: serializer.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-06-28 21:20:25 (CST)
# Last Update: Sunday 2019-06-30 14:18:31 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_maple.serializer import Serializer


class BucketSerializer(Serializer):
    class Meta:
        exclude = ["paths"]


class FileSerializer(Serializer):
    class Meta:
        exclude = ["path", "hash"]
        extra = ["url"]


class FilePathSerializer(Serializer):
    class Meta:
        exclude = [
            "parent_path", "files", "bucket", "child_paths", "bucket_id"
        ]
