#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:40 (CST)
# Last Update: Wednesday 2019-07-10 19:22:40 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import Blueprint
from maple.extension import csrf
from maple.utils import lazyconf

from . import api, config
from .router import FileShowView

site = Blueprint('storage', __name__)

site.add_url_rule(
    "/",
    defaults={"filename": "default/index.html"},
    view_func=FileShowView.as_view("index"),
)
site.add_url_rule(
    "/<path:filename>",
    view_func=FileShowView.as_view("show"),
)


def init_app(app):
    lazyconf(app, config, "STORAGE")
    csrf.exempt(site)
    api.init_api(site)
    app.register_blueprint(site, subdomain=config.SUBDOMAIN)
