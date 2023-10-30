#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：develop.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/10/30 23:13 
'''
from .base import *  # NOQA
# NOQA  告诉PEP8规范工具，这个不需要检测

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}