#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：forms.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/10/29 10:25 
'''
# 提交数据的功能
from __future__ import unicode_literals

from django import forms

from .models import Student


class StudentForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=128)
    sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
    profession = forms.CharField(label='职业', max_length=128)
    email = forms.EmailField(label='邮箱', max_length=128)
    qq = forms.CharField(label='QQ', max_length=128)
    phone = forms.CharField(label='手机', max_length=128)