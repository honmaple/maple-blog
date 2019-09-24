#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: router.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:36 (CST)
# Last Update: Wednesday 2019-09-11 12:15:53 (CST)
#          By:
# Description:
# ********************************************************************************
import os
from datetime import datetime as dt
from datetime import timedelta

from flask import abort, make_response, request, send_from_directory
from maple.utils import MethodView

from . import config
from .util import file_is_image, gen_thumb_image, referer_is_block


class FileShowView(MethodView):
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
