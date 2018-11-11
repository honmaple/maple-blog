#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: response.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-11-06 10:23:21 (CST)
# Last Update: Tuesday 2018-11-06 10:29:03 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import make_response, jsonify, render_template


class PageInfo(object):
    def __init__(self, ins, page, number):
        self.ins = ins
        self.page = page if page > 0 else 1
        if number == -1:
            self.number = 1000
        else:
            self.number = number if number > 0 else 10

        self.pages = self._pages

    @property
    def _pages(self):
        length = len(self.ins)
        if length % self.number == 0:
            return length // self.number
        return length // self.number + 1

    @property
    def data(self):
        pages = self.pages
        if self.page > pages:
            self.page = pages
        return self.ins[(self.page - 1) * self.number:self.page * self.number]


class HTTPResponse(object):
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_ERROR = 500

    def __init__(self, status_code=200, message="", data=None, pageinfo=None):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.pageinfo = pageinfo

    def to_dict(self):
        return {
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data,
            "pageinfo": self.pageinfo
        }

    def to_response(self):
        resp = dict(message=self.message)
        if self.data is not None:
            resp.update(data=self.data)
        if self.pageinfo is not None:
            resp.update(pageinfo=self.pageinfo)
        return make_response(jsonify(**resp), self.status_code)


class HTTP(object):
    @classmethod
    def OK(cls, message="ok", data=None, pageinfo=None):
        return HTTPResponse(
            HTTPResponse.OK,
            message,
            data,
            pageinfo,
        ).to_response()

    @classmethod
    def BAD_REQUEST(cls, message="bad request", data=None):
        return HTTPResponse(
            HTTPResponse.BAD_REQUEST,
            message,
            data,
        ).to_response()

    @classmethod
    def UNAUTHORIZED(cls, message="unauthorized", data=None):
        return HTTPResponse(
            HTTPResponse.UNAUTHORIZED,
            message,
            data,
        ).to_response()

    @classmethod
    def FORBIDDEN(cls, message="forbidden", data=None):
        return HTTPResponse(
            HTTPResponse.FORBIDDEN,
            message,
            data,
        ).to_response()

    @classmethod
    def NOT_FOUND(cls, message="not found", data=None):
        return HTTPResponse(
            HTTPResponse.NOT_FOUND,
            message,
            data,
        ).to_response()

    @classmethod
    def SERVER_ERROR(cls, message="internal server error", data=None):
        return HTTPResponse(
            HTTPResponse.SERVER_ERROR,
            message,
            data,
        ).to_response()

    @classmethod
    def HTML(cls, template, **kwargs):
        return render_template(template, **kwargs)
