#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: forms.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-10-29 07:09:54
# *************************************************************************
from flask import flash, jsonify


def flash_errors(form):
    for field, errors in form.errors.items():
        flash(u"%s %s" % (getattr(form, field).label.text, errors[0]))
        break


def return_errors(form):
    for field, errors in form.errors.items():
        data = (u"%s %s" % (getattr(form, field).label.text, errors[0]))
        break
    return jsonify(judge=False, error=data)
