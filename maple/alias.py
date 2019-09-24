#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: alias.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-13 00:29:40 (CST)
# Last Update: Tuesday 2019-09-24 18:09:14 (CST)
#          By:
# Description:
# ********************************************************************************
import hashlib
from functools import wraps

from flask import abort, current_app, request
from werkzeug.routing import MethodNotAllowed, NotFound, RequestRedirect

FUNCTION = dict()


def view_function_cache(func):
    @wraps(func)
    def _view_function(url, method='GET'):
        if len(FUNCTION) > 100:
            for k, v in FUNCTION.items():
                if v is None:
                    FUNCTION.pop(k)

        key = method + url
        key = str(hashlib.md5(key.encode("UTF-8")).hexdigest())
        if key in FUNCTION:
            return FUNCTION[key]
        FUNCTION[key] = func(url, method)
        return FUNCTION[key]

    return _view_function


# https://stackoverflow.com/questions/38488134/get-the-flask-view-function-that-matches-a-url
@view_function_cache
def get_view_function(url, method='GET'):
    adapter = current_app.url_map.bind('localhost')
    try:
        match = adapter.match(url, method=method)
    except RequestRedirect as e:
        # recursively match redirects
        return get_view_function(e.new_url, method)
    except (MethodNotAllowed, NotFound):
        # no match
        return None

    try:
        # return the view function and arguments
        return current_app.view_functions[match[0]], match[1]
    except KeyError:
        # no view is associated with the endpoint
        return None


def redirect_en(uri):
    view_function = get_view_function(
        "/" + uri,
        request.method,
    )
    if view_function is None:
        abort(404)
    request.environ["HTTP_ACCEPT_LANGUAGE"] = "en-US,en;q=0.5"
    return view_function[0](**view_function[1])


def init_app(app):
    app.add_url_rule(
        "/en",
        defaults={"uri": ""},
        view_func=redirect_en,
    )

    app.add_url_rule(
        "/en/<path:uri>",
        view_func=redirect_en,
    )
    # @app.before_request
    # def before_request():
    #     if request.path.startswith("/en/"):
    #         request.environ["HTTP_ACCEPT_LANGUAGE"] = "en-US,en;q=0.5"

    # url_map = list(app.url_map.iter_rules())
    # for rule in url_map:
    #     app.add_url_rule("/en" + rule.rule, rule.endpoint, alias=True)
