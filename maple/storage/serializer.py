#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: serializer.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-06-28 21:20:25 (CST)
# Last Update: Wednesday 2019-07-10 00:17:25 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_maple.serializer import Serializer


class BucketSerializer(Serializer):
    class Meta:
        exclude = ["paths"]


class FileSerializer(Serializer):
    class Meta:
        exclude = ["path", "hash", "path_id"]
        extra = ["url"]


class FilePathSerializer(Serializer):
    class Meta:
        exclude = [
            "parent_id",
            "parent_path",
            "files",
            "bucket",
            "child_paths",
            "bucket_id",
        ]
        extra = ["size"]
