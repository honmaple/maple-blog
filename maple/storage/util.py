#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: util.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 17:11:51 (CST)
# Last Update: Wednesday 2019-07-10 21:14:01 (CST)
#          By:
# Description:
# ********************************************************************************
import os
import re
from hashlib import sha512
from io import BytesIO
from re import match

from PIL import Image as ImagePIL
from werkzeug.urls import url_parse
from werkzeug.utils import PY2, text_type

from . import config

_windows_device_files = ('CON', 'AUX', 'COM1', 'COM2', 'COM3', 'COM4', 'LPT1',
                         'LPT2', 'LPT3', 'PRN', 'NUL')
_filename_gbk_strip_re = re.compile(r"[^\u3e00-\u9fa5()A-Za-z0-9_.-]")


class Disk(object):
    def __init__(self, f):
        self.f = f

    def write(self):
        pass

    def rename(self):
        pass

    def remove(self):
        pass


def secure_filename(filename):
    if isinstance(filename, text_type):
        from unicodedata import normalize
        filename = normalize('NFKD', filename).encode('utf-8', 'ignore')
        if not PY2:
            filename = filename.decode('utf-8')
    for sep in os.path.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, ' ')
    filename = str(_filename_gbk_strip_re.sub('', '_'.join(
        filename.split()))).strip('._')

    if os.name == 'nt' and filename and \
       filename.split('.')[0].upper() in _windows_device_files:
        filename = '_' + filename
    return filename


def gen_hash(file_data):
    sha = sha512()
    sha.update(file_data.read())
    return sha.hexdigest()


def gen_size(file_data):
    if file_data.content_length:
        return file_data.content_length

    try:
        pos = file_data.tell()
        file_data.seek(0, 2)  # seek to end
        size = file_data.tell()
        file_data.seek(pos)  # back to original position
        return size
    except (AttributeError, IOError):
        pass
    return 0


def gen_thumb_image(path, width=0, height=0, filetype='webp'):
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


def list_files(path):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isfile(f):
            files.append(f)
            continue
        files.extend(list_files(f))
    return files


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


def referer_is_block(request):
    referrer = request.referrer
    if referrer is None:
        return False

    hostname = url_parse(referrer).host
    for r in config.ALLOWED_REFERER:
        if r.startswith("*.") and match(".*." + r.split(".", 1)[1], hostname):
            return False
        if r == hostname:
            return False
    return True
