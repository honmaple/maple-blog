#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:40 (CST)
# Last Update: Thursday 2019-07-04 14:26:07 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import Blueprint
from maple.extension import csrf
from maple.utils import lazyconf

from . import api, config
from .router import FileShowView

site = Blueprint('storage', __name__)

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


def init_app(app):
    lazyconf(app, config, "STORAGE")
    csrf.exempt(site)
    api.init_api(site)
    app.register_blueprint(site, subdomain=config.SUBDOMAIN)
