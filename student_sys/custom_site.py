#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：custom_site.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/11/1 0:26 
'''
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Student_sys'
    site_title = 'student管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')