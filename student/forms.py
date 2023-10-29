#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：forms.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/10/29 10:27 
'''
from __future__ import unicode_literals

from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    # clean_qq 就是Django会自动调用，来处理每个字段的方法
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        # 验证失败，可以通过raise forms.ValidationError('必须是数字！')
        # 的方式返回错误信息，这个信息会存储在form中，最终会被我们渲染到页面上。

        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )