#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：adminforms.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/11/1 0:24 
'''
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)