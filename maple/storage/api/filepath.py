#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: filepath.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-03 21:39:57 (CST)
# Last Update: Monday 2019-09-23 17:11:26 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from flask_maple.response import HTTP
from maple.utils import AuthMethodView
from maple.storage.db import File, FilePath
from maple.storage.serializer import FilePathSerializer
from maple.storage.util import file_is_allowed, gen_hash, secure_filename
from maple.utils import filter_maybe, is_true, update_maybe, check_params


class FilePathListView(AuthMethodView):
    def get(self, bucket):
        data = request.data
        user = request.user
        page, number = self.pageinfo

        bucket = user.buckets.filter_by(
            name=bucket).get_or_404("bucket not found")
        path = request.data.get("path", "/")

        params = filter_maybe(data, {
            "name": "name__contains",
        })
        rootpath = bucket.get_root_path(path)
        paths = rootpath.child_paths.filter_by(**params).paginate(page, number)
        serializer = FilePathSerializer(paths)
        return HTTP.OK(data=serializer.data)

    @check_params(["path"])
    def post(self, bucket):
        user = request.user
        bucket = user.buckets.filter_by(
            name=bucket).get_or_404("bucket not found")

        path = request.data["path"]
        filepath = bucket.get_root_path(path, True)
        serializer = FilePathSerializer(filepath)
        return HTTP.OK(data=serializer.data)

    @check_params(["path"])
    def put(self, bucket):
        data = request.data
        user = request.user
        bucket = user.buckets.filter_by(
            name=bucket).get_or_404("bucket not found")

        path = data["path"]
        filepath = bucket.get_root_path(path)
        if not filepath or filepath.is_root_path:
            msg = "{0} path not found"
            return HTTP.BAD_REQUEST(message=msg)

        action = data.get("action", "rename")
        if action not in ["rename", "move", "copy"]:
            return HTTP.BAD_REQUEST()

        if action == "rename":
            newname = data.get("newname")
            if not newname or newname == filepath.name:
                return HTTP.OK(message="filepath not change")
            serializer = FilePathSerializer(filepath.rename(newname))
            return HTTP.OK(data=serializer.data)

        newpath = data.get("newpath")
        if not newpath:
            return HTTP.BAD_REQUEST(message="newpath is required")

        newfilepath = bucket.get_root_path(newpath)
        if not newfilepath:
            msg = "{0} path not found"
            return HTTP.BAD_REQUEST(message=msg)

        if action == "move":
            nfilepath = filepath.move(newfilepath)
        else:
            nfilepath = filepath.copy(newfilepath)

        serializer = FilePathSerializer(nfilepath)
        return HTTP.OK(data=serializer.data)

    @check_params(["path"])
    def delete(self, bucket):
        data = request.data
        user = request.user
        bucket = user.buckets.filter_by(
            name=bucket).get_or_404("bucket not found")

        path = data["path"]
        filepath = bucket.get_root_path(path)
        if not filepath:
            msg = "{0} path not found"
            return HTTP.BAD_REQUEST(message=msg)
        filepath.delete()
        return HTTP.OK()
