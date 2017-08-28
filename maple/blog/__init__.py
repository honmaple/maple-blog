#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-17 13:49:48 (CST)
# Last Update:星期日 2017-8-27 22:58:3 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import (BlogListView, BlogView, RssView, ArchiveView)
from .filters import (safe_markdown, random_fortune, tag_archives,
                      category_archives, time_archives, orgmode)

site = Blueprint('blog', __name__)
bloglist_view = BlogListView.as_view('bloglist')
site.add_url_rule('', view_func=bloglist_view)
site.add_url_rule('/', view_func=bloglist_view)
site.add_url_rule('/<int:blogId>', view_func=BlogView.as_view('blog'))
site.add_url_rule('/archives', view_func=ArchiveView.as_view('archive'))
site.add_url_rule('/rss', view_func=RssView.as_view('rss'))

site.add_app_template_global(random_fortune)
site.add_app_template_global(tag_archives)
site.add_app_template_global(category_archives)
site.add_app_template_global(time_archives)
site.add_app_template_filter(safe_markdown)
site.add_app_template_filter(orgmode)


def init_app(app):
    app.register_blueprint(site, url_prefix='/blog')
