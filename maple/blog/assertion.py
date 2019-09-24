#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: assertion.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-08-17 00:48:47 (CST)
# Last Update: Tuesday 2019-09-24 11:19:53 (CST)
#          By:
# Description:
# ********************************************************************************
from maple.assertion import Assert


class ArticleAssert(Assert):
    def assert_title(self, value):
        self.assertRequire(value, "title is required")

    def assert_content(self, value):
        self.assertRequire(value, "content is required")

    def assert_content_type(self, value):
        self.assertIn(value, ["0", "1"])

    def assert_category(self, value):
        pass

    def assert_tags(self, value):
        pass


class TimeLineAssert(Assert):
    def assert_content(self, value):
        self.assertRequire(value)
        self.assertLength(value, 4)
