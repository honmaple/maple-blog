#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: bucket.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:36 (CST)
# Last Update: Monday 2019-09-23 17:11:18 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from flask_maple.response import HTTP
from maple.utils import AuthMethodView
from maple.storage.db import Bucket
from maple.storage.serializer import BucketSerializer
from maple.utils import check_params, filter_maybe, update_maybe


class BucketListView(AuthMethodView):
    def get(self):
        data = request.data
        user = request.user
        page, number = self.pageinfo

        params = filter_maybe(data, {"name": "name__contains"})
        ins = user.buckets.filter_by(**params).paginate(page, number)
        serializer = BucketSerializer(ins)
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

        rep = BucketSerializer(bucket).data
        return HTTP.OK(data=rep)


class BucketView(AuthMethodView):
    def get(self, pk):
        user = request.user
        ins = user.buckets.filter_by(id=pk).get_or_404("bucket not found")
        rep = BucketSerializer(ins).data
        return HTTP.OK(data=rep)

    def put(self, pk):
        user = request.user
        data = request.data

        ins = user.buckets.filter_by(id=pk).get_or_404("bucket not found")
        ins = update_maybe(ins, data, ["name", "description"])
        ins.save()

        rep = BucketSerializer(ins).data
        return HTTP.OK(data=rep)

    def delete(self, pk):
        user = request.user
        ins = user.buckets.filter_by(id=pk).get_or_404("bucket not found")
        ins.delete()
        return HTTP.OK()
