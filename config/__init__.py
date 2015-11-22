#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 07:20:38
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
import os


def load_config():
    """加载配置类"""
    try:
        from .development import DevelopmentConfig
        return DevelopmentConfig
    except ImportError as e:
        from .default import Config
        return Config
