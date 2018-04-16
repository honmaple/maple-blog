#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: validator.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-27 23:14:48 (CST)
# Last Update: 星期一 2018-02-05 13:34:41 (CST)
#          By:
# Description:
# **************************************************************************
class ValidationException(Exception):
    pass


class And(object):
    def __init__(self, validators):
        self.validators = validators

    def is_valid(self, args, strict=False):
        return validation(self.validators, args, strict)


class Or(And):
    def is_valid(self, args, strict=False):
        for validator in self.validators:
            result = validation([validator], args, strict)
            if result is True:
                break
        return result


class Validator(object):
    _callback = {
        '200': 'OK',
        '401': 'Parameters Error',
        '403': 'Forbbiden',
        '404': 'Not Found'
    }

    def __init__(self,
                 name,
                 alias=None,
                 required=False,
                 equal=None,
                 length=None,
                 integer=None,
                 boolean=None,
                 in_=[],
                 type=str,
                 help='',
                 custom=None,
                 default=True,
                 callback=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.equal = equal
        self.length = length
        self.integer = integer
        self.boolean = boolean
        self.in_ = in_
        self.type = type
        self.help = help
        self.callback = callback
        self.custom = custom
        self.default = default
        self.validators = []

    def convert(self, value):
        if value is None and self.required:
            self.callback = self.callback_required()
            raise ValidationException(self.callback)
        return self.type(value)

    def validate_custom(self, value):
        if self.custom is not None:
            return self.custom(value)
        return self.default

    def validate_boolean(self, value):
        if self.boolean is not None:
            if isinstance(self.boolean, (list, tuple)):
                return value in self.boolean
            return value in ['true', 'yes', '1', True]
        return self.default

    def callback_boolean(self):
        return "{} is not valid boolean value".format(self.name)

    def validate_integer(self, value):
        if self.integer is not None:
            value = int(value)
            if callable(self.integer):
                return self.integer(value)
            return value == self.integer
        return self.default

    def callback_integer(self):
        return "{} parameters error".format(self.name)

    def validate_length(self, value):
        if self.length is not None:
            value = str(value)
            if callable(self.length):
                return self.length(len(value))
            return len(value) == self.length
        return self.default

    def callback_length(self):
        return "{}'s length is error".format(self.name)

    def validate_in(self, value):
        if self.in_:
            return value in self.in_
        return self.default

    def callback_in(self):
        return '{} must in {}'.format(self.name, self.in_)

    def validate_equal(self, value):
        if self.equal is not None:
            return value == self.equal
        return self.default

    def callback_equal(self):
        return '{} must equal to {}'.format(self.name, self.equal)

    def validate_required(self, value):
        if self.required:
            return False if not value else True
        return self.default

    def callback_required(self):
        return '{} is required'.format(self.name)

    def validate_type(self, value):
        return type(value) == self.type

    def callback_type(self):
        return '{} type is not {}'.format(self.name, self.type)

    def add_validator(self, *args, **kwargs):
        validator = Validator(*args, **kwargs)
        self.validators.append(validator)

    def is_valid(self, args, strict=False):
        if not self.validators:
            return validation([self], args, strict)
        return validation(self.validators, args, strict)

    def __call__(self, value):
        value = self.convert(value)
        validates = ['required', 'type', 'equal', 'in', 'length', 'integer',
                     'boolean', 'custom']
        _callback = self.callback
        for validate in validates:
            self.callback = _callback
            validate = 'validate_' + validate
            callback = 'callback_' + validate
            if hasattr(self, callback):
                self.callback = getattr(self, callback)()
            assert getattr(self, validate)(value) is True

    def __str__(self):
        return '{} validation'.format(self.name)


def validation(validators, args, strict=False):
    if callable(args):
        args = args()
    for validator in validators:
        if isinstance(validator, (list, tuple)):
            validator = And(validator)
        if isinstance(validator, And):
            result = validator.is_valid(args, strict)
            if result is True:
                continue
            return result
        elif isinstance(validator, Or):
            result = validator.is_valid(args, strict)
            if result is True:
                break
            return result
        name = validator.name
        if validator.alias is not None:
            name = validator.alias
        value = args.get(name)
        if strict and value is None:
            raise ValidationException('{} not exists'.format(name))
        try:
            validator(value)
        except (ValueError, TypeError):
            return '{} cannot be converted to {}'.format(
                value, validator.type.__name__)
        except (AssertionError, ValidationException):
            return 'callback' if validator.callback is None else validator.callback
    return True
