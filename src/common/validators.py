#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: validator.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-01-12 16:08:18 (CST)
# Last Update:星期四 2017-1-12 18:4:48 (CST)
#          By:
# Description:
# **************************************************************************
from re import compile


class ValidatorError(ValueError):
    def __init__(self, key, message):
        self.key = key
        self.message = message
        super(ValidatorError, self).__init__(key, message)


class Validator(object):
    def __call__(self, value):
        self.value = value
        return self.validate(value)


class TypeValidator(Validator):
    def __init__(self, key):
        self.key = key
        self.message = 'must be %s' % key

    def validate(self, value):
        if isinstance(value, self.key):
            return True


class RequiredValidator(Validator):
    def __init__(self, key):
        self.key = key
        self.message = 'is required'

    def validate(self, value):
        if self.key and value:
            return True


class LengthValidator(Validator):
    def __init__(self, key):
        self.key = key
        self.message = 'length must be %s' % key

    def validate(self, value):
        if isinstance(value, str):
            value = len(value)
        if callable(self.key):
            return self.key(value)
        return value == self.key


class UniqueValidator(Validator):
    def __init__(self, key):
        self.key = key
        self.message = 'must be %s' % key

    def validate(self, value):
        return self.key


class EqualValidator(Validator):
    def __init__(self, key):
        self.key = key
        self.message = 'must be equal to %s' % key

    def validate(self, value):
        if callable(self.key):
            self.key = self.key()
        return value == self.key


validator_choice = {
    'type': TypeValidator,
    'length': LengthValidator,
    'equal': EqualValidator,
    'required': RequiredValidator
}


class Validate(object):
    def __init__(self, kwargs):
        self.kwargs = kwargs

    def is_val(self):
        for m in self.__class__.__dict__:
            value = self.kwargs.pop(m, None)
            if not m.startswith('__'):
                validator = getattr(self, m)
                callback = validator.pop('callback', None)
                for k, v in validator.items():
                    if isinstance(v, (tuple, list)):
                        callback = v[1]
                        v = v[0]
                    valid = validator_choice[k](v)
                    result = valid(value)
                    if not callback:
                        callback = valid.message
                    if not result:
                        raise ValidatorError(m, callback)
        return True


if __name__ == '__main__':

    class LoginValidator(Validate):
        '''
        type: string,int,phone,email,url
        length: lambda n:len(n) > 9
        required: True,False
        '''
        username = {
            'required': (True, u'sssss'),
            'type': str,
            'length': lambda n: n < 10,
            'callback': '11111'
        }

    data = {'username': ''}
    a = LoginValidator(data).is_val()
    print(a)
