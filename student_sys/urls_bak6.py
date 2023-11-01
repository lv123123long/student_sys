#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/11/1 0:28 
'''
from django.conf.urls import url
from django.contrib import admin

from .custom_site import custom_site

urlpatterns = [
    url(r'^super_admin/', admin.site.urls),
    url(r'^admin/', custom_site.urls),
]