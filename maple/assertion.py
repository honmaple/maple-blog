#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: assertion.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-13 15:05:53 (CST)
# Last Update: Tuesday 2019-09-24 11:23:46 (CST)
#          By:
# Description:
# ********************************************************************************
import re
from functools import wraps

from flask import abort as flask_abort
from flask import request
from flask_maple.response import HTTP


def assert_request(assertion, include=[], exclude=[]):
    def _assert_request(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            data = request.data
            resp = assertion(data, include, exclude)()
            if resp is not None:
                return resp
            return func(*args, **kwargs)

        return decorator

    return _assert_request


class Assert(object):
    def __init__(self, data=dict(), include=[], exclude=[], abort=None):
        self.data = data
        self.asserts = {
            i.split("_", 2)[1]: [i]
            for i in dir(self) if i.startswith('assert_')
        }
        self._include = include
        self._exclude = exclude
        self._abort = abort

    def abort(self, key, value, message):
        if self._abort is not None:
            if callable(self._abort):
                return self._abort(key, value, message)
            return self._abort
        if not message:
            message = "{0} params error".format(key)
        return flask_abort(HTTP.BAD_REQUEST(message=message))

    def add(self, key, assertion, *args, **kwargs):
        # assertion.add("username", "assertRequire")
        # assertion.add("password", "assertRequire", "密码不能为空")
        # assertion.add("password", "assertLength", 5, 20)
        assert hasattr(self, assertion)

        def _assert(value):
            assert getattr(self, assertion)(value, *args, **kwargs)

        self.asserts.setdefault(key, [])
        self.asserts[key].append(_assert)

    def assertOr(self, funcs=[], msg=None):
        raise_errors = []
        for func in funcs:
            try:
                func()
            except AssertionError as e:
                raise_errors.append(e)

        if funcs and len(raise_errors) == len(funcs):
            if msg is None:
                raise raise_errors[0]
            raise AssertionError(msg) from raise_errors[0]

    def assertAnd(self, funcs=[], msg=None):
        for func in funcs:
            try:
                func()
            except AssertionError as e:
                if msg is None:
                    raise
                raise AssertionError(msg) from e

    def assertRequire(self, key, msg=None):
        if not msg:
            msg = "{0} is null".format(key)
        if not bool(key):
            raise AssertionError(msg)

    def assertIn(self, key, value, msg=None):
        if not msg:
            msg = "{0} not in {1}".format(key, value)
        if key not in value:
            raise AssertionError(msg)

    def assertType(self, key, value, msg=None):
        if not msg:
            msg = "{0}'s type is not {1}".format(key, value)
        if not isinstance(key, value):
            raise AssertionError(msg)

    def assertEqual(self, key, value, ignore_case=False, msg=None):
        if ignore_case:
            key, value = key.lower(), value.lower()

        if not msg:
            msg = "{0} should be equal to {1}".format(key, value)

        if key == value:
            raise AssertionError(msg)

    def assertLength(self, key, min_length=0, max_length=0, msg=None):
        if not msg and min_length == max_length:
            msg = "{0}'s length should be equal to {1}".format(key, min_length)
        elif not msg and min_length == 0:
            msg = "{0}'s length should be less than {1}".format(
                key, max_length)
        elif not msg and max_length == 0:
            msg = "{0}'s length should be greater than {1}".format(
                key, min_length)
        elif not msg:
            msg = "{0}'s length should be between with {1} to {2}".format(
                key, min_length, max_length)

        if key is None:
            key = ""

        length = len(key)

        if length < min_length or (max_length > 0 and length > max_length):
            raise AssertionError(msg)

    def assertURL(self, value, msg=None):
        if not msg:
            msg = "{0} is not effective url".format(value)
        key = r'^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$'
        self.assertRegex(value, key, msg)

    def assertEmail(self, value, msg=None):
        if not msg:
            msg = "{0} is not effective email".format(value)
        key = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
        self.assertRegex(value, key, msg)

    def assertRegex(self, key, value, msg=None):
        if not msg:
            msg = "{0} can't match with {1}".format(value, key)
        if not re.match(value, key):
            raise AssertionError(msg)

    def __call__(self):
        for key, funcs in self.asserts.items():
            if self._include and key not in self._include:
                continue
            if self._exclude and key in self._exclude:
                continue
            value = self.data.get(key)
            for func in funcs:
                if isinstance(func, str):
                    func = getattr(self, func)
                try:
                    func(value)
                except AssertionError as e:
                    return self.abort(key, value, e)


# if __name__ == '__main__':

#     class UserAssert(Assert):
#         def assert_username(self, value):
#             self.assertRequire(value, "用户名不能为空")
#             self.assertLength(value, 4, 20, "用户名长度必须大于等于5")

#         def assert_password(self, value):
#             self.assertRequire(value, "密码不能为空")
#             self.assertLength(value, 5, 20, "密码长度必须大于等于5")

#             funcs = [
#                 lambda: self.assertRequire(value, "密码不能为空"),
#                 lambda: self.assertLength(value, 5, 20, "密码长度必须大于等于5")
#             ]
#             self.assertOr(funcs, "用户名错误")
#             self.assertAnd(funcs, "用户名错误1")

#     assertion = UserAssert({"username": "username", "password": "pass"})()
