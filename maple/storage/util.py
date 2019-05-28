#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: util.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 17:11:51 (CST)
# Last Update: Friday 2019-06-07 14:59:22 (CST)
#          By:
# Description:
# ********************************************************************************
from hashlib import sha512
from io import BytesIO
from PIL import Image as ImagePIL
from . import config


class Disk(object):
    def __init__(self, f):
        self.f = f

    def write(self):
        pass

    def rename(self):
        pass

    def remove(self):
        pass


def gen_hash(image):
    sha = sha512()
    # while True:
    #     data = f.read(block_size)
    #     if not data:
    #         break
    # sha1.update(data)
    sha.update(image.read())
    return sha.hexdigest()


def gen_thumb_image(path, width=0, height=0, filetype='PNG'):
    '''
    生成缩略图
    '''
    width = min(1024, width)
    height = min(1024, height)
    img = ImagePIL.open(path)
    if width and not height:
        height = float(width) / img.size[0] * img.size[1]
    if not width and height:
        width = float(height) / img.size[1] * img.size[0]
    stream = BytesIO()
    img.thumbnail((width, height), ImagePIL.ANTIALIAS)
    img.save(stream, format=filetype, optimize=True)
    return stream


def file_is_allowed(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in config.UPLOAD_ALLOWED_EXTENSIONS


def file_is_image(filename):
    if "." not in filename:
        return False
    file_type = filename.rsplit(".", 1)[1].lower()
    if file_type in ["png", "jpg", "jpeg"]:
        return True
    return False
