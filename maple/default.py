#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: default.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-09 22:34:08 (CST)
# Last Update: Friday 2019-06-07 22:26:12 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_babel import lazy_gettext as _

SITE = {
    'title': _('紅楓'),
    'subtitle': _('爱情诚可贵，自由价更高'),
    "author": "lin.jiang",
}

EXTENSION = {"login": False}
SUBDOMAIN = {"static": True}
HEADER = [
    {
        "name": _("Poem"),
        "url": "https://poem.honmaple.com"
    },
    {
        "name": _("Cloud"),
        "url": "https://cloud.honmaple.com"
    },
    {
        "name": _("TimeLine"),
        "url": "blog.timelines"
    },
    {
        "name": _("Archives"),
        "url": "blog.archives"
    },
    {
        "name": _("About me"),
        "url": "about"
    },
]

FOOTER = {
    "copyright": "© 2015-2019 honmaple",
    "links": [{
        "name": _("Friends"),
        "url": "friend"
    }, {
        "name": _("Contact"),
        "url": "contact"
    }, {
        "name": _("Poem"),
        "url": "https://poem.honmaple.com"
    }, {
        "name": _("TimeLine"),
        "url": "blog.timelines"
    }],
    "socials": [
        {
            "name": "GitHub",
            "icon": "fa-github",
            "url": "https://github.com/honmaple"
        },
        {
            "name": "MINE",
            "icon": "fa-globe",
            "url": "https://honmaple.me"
        },
        {
            "name": "Mail",
            "icon": "fa-envelope",
            "url": "mailto:mail@honmaple.com"
        },
    ]
}

INFO = [{
    "name": "Rss",
    "icon": "fa-rss",
    "url": "/rss"
}, {
    "name": "MINE",
    "icon": "fa-globe",
    "url": "https://honmaple.me"
}, {
    "name": "GitHub",
    "icon": "fa-github",
    "url": "https://github.com/honmaple"
}, {
    "name": "Mail",
    "icon": "fa-envelope",
    "url": "mailto:mail@honmaple.com"
}]
