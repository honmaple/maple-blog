#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 07:20:38
# *************************************************************************


def load_config():
    try:
        from .development import DevelopmentConfig
        return DevelopmentConfig
    except ImportError as e:
        from .default import Config
        return Config
