#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: router.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:36 (CST)
# Last Update: Sunday 2019-06-16 19:21:34 (CST)
#          By:
# Description:
# ********************************************************************************
import os
from datetime import datetime as dt
from datetime import timedelta

from flask import abort, make_response, request, send_from_directory

from flask_maple.response import HTTP
from flask_maple.serializer import Serializer
from flask_maple.views import IsAuthMethodView
from maple.utils import MethodView, check_params, filter_maybe, update_maybe

from . import config
from .db import Bucket, File
from .util import (file_is_allowed, file_is_image, gen_hash, gen_thumb_image,
                   referer_is_block, secure_filename)


class BucketListView(IsAuthMethodView):
    def get(self):
        data = request.data
        user = request.user
        page, number = self.pageinfo

        params = filter_maybe(data, {"name": "name__contains"})
        ins = user.buckets.filter_by(**params).paginate(page, number)
        serializer = Serializer(ins)
        return HTTP.OK(data=serializer.data)

    @check_params(["name"])
    def post(self):
        data = request.data
        name = data.get('name')
        description = data.get('description')
        if Bucket.query.filter_by(name=name).exists():
            return HTTP.BAD_REQUEST(message="bucket is exists")

        bucket = Bucket(name=name)
        if description:
            bucket.description = description
        bucket.save()

        rep = Serializer(bucket).data
        return HTTP.OK(data=rep)


class BucketView(IsAuthMethodView):
    def get(self, pk):
        user = request.user
        ins = user.buckets.filter_by(id=pk).get_or_404("bucket not found")
        rep = Serializer(ins).data
        return HTTP.OK(data=rep)

    def put(self, pk):
        user = request.user
        data = request.data

        ins = user.buckets.filter_by(id=pk).get_or_404("bucket not found")
        ins = update_maybe(ins, data, ["name", "description"])
        ins.save()

        rep = Serializer(ins).data
        return HTTP.OK(data=rep)

    def delete(self, pk):
        user = request.user
        ins = user.buckets.filter_by(id=pk).get_or_404("bucket not found")
        ins.delete()
        return HTTP.OK()


class FileListView(IsAuthMethodView):
    def get(self, bucket):
        data = request.data
        user = request.user
        page, number = self.pageinfo

        bucket = user.buckets.filter_by(
            id=bucket).get_or_404("bucket not found")

        params = filter_maybe(data, {
            "name": "name__contains",
            "path": "path",
            "type": "file_type"
        })

        ins = bucket.files.filter_by(**params).paginate(page, number)
        serializer = Serializer(ins)
        return HTTP.OK(data=serializer.data)

    def post(self, bucket):
        user = request.user
        bucket = user.buckets.filter_by(
            id=bucket).get_or_404("bucket not found")

        files = request.files.getlist('files')
        if files:
            return self.post_with_multi(user, bucket, files)
        return self.post_with_one(user, bucket)

    def post_with_one(self, user, bucket, f=None):
        if not f:
            f = request.files.get("file")
        if not f:
            return HTTP.BAD_REQUEST(message="file is null")

        filename = secure_filename(f.filename)
        if not file_is_allowed(filename):
            msg = '{name} 不允许的扩展'.format(name=filename)
            return HTTP.BAD_REQUEST(message=msg)

        file_type = f.content_type
        hash = gen_hash(f)
        ins = File.query.filter_by(hash=hash, user=user).first()
        if not ins:
            ins = File(
                hash=hash,
                path="",
                file_type=file_type,
                user=user,
                bucket=bucket)
        # 保存到磁盘中
        # http://stackoverflow.com/questions/42569942/calculate-md5-from-werkzeug-datastructures-filestorage-but-saving-the-object-as
        path = os.path.join(config.UPLOAD_FOLDER, filename)
        f.seek(0)
        f.save(path)
        rep = Serializer(ins).data
        return HTTP.OK(data=rep)

    def post_with_multi(self, user, bucket, files):
        fail = []
        for f in files:
            resp = self.post_with_one(Bucket, f)
            if resp.status_code != 200:
                fail.append(resp.data)
        return HTTP.OK(data=fail)


class FileView(IsAuthMethodView):
    def get(self, pk):
        user = request.user
        ins = File.query.filter_by(
            id=pk, bucket__user_id=user.id).get_or_404("file not found")
        rep = Serializer(ins).data
        return HTTP.OK(data=rep)

    def put(self, pk):
        data = request.data
        user = request.user
        ins = File.query.filter_by(
            id=pk, bucket__user_id=user.id).get_or_404("file not found")
        ins = update_maybe(ins, data, ["name"])
        ins.save()
        rep = Serializer(ins).data
        return HTTP.OK(data=rep)

    def delete(self, pk):
        user = request.user
        ins = File.query.filter_by(
            id=pk, bucket__user_id=user.id).get_or_404("file not found")
        ins.delete()
        return HTTP.OK()


class FileShowView(MethodView):
    cache = True
    cache_time = 3600

    def render_image(self, filename):
        '''
        默认设置为webp, 减少传输大小
        '''
        typ = request.args.get("type")
        width = request.args.get("width", 0, type=int)
        height = request.args.get("height", 0, type=int)

        if typ == "iloveyou":  # 哈哈
            return send_from_directory(config.UPLOAD_FOLDER, filename)

        if typ == "mini":
            width, height = 120, 0
        elif typ == "small":
            width, height = 360, 0
        elif typ == "thumb":
            width, height = 600, 0
        elif typ == "show":
            width, height = 960, 0
        elif width == height == 0:
            width, height = 960, 0

        img = os.path.join(config.UPLOAD_FOLDER, filename)
        stream = gen_thumb_image(img, width, height)
        buf_value = stream.getvalue()
        response = make_response(buf_value)

        max_age = 30 * 3600 * 24
        response.mimetype = "image/webp"
        # 不要设置last_modified, 避免浏览器与服务端多一次交互
        # response.last_modified = os.path.getmtime(img)
        response.expires = dt.utcnow() + timedelta(seconds=max_age)
        # response.cache_control.public = True
        response.cache_control.max_age = max_age
        response.add_etag()
        return response.make_conditional(request)

    def get(self, filename):
        if referer_is_block(request):
            abort(403)
        if not os.path.exists(os.path.join(config.UPLOAD_FOLDER, filename)):
            abort(404)
        if file_is_image(filename):
            return self.render_image(filename)
        return send_from_directory(config.UPLOAD_FOLDER, filename)
