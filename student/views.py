#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：views.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/10/29 21:02 
'''
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .models import Student
from .forms import StudentForm


class IndexView(View):
    # 继承了View类
    template_name = 'index.html'

    def get_context(self):
        students = Student.objects.all()
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        # update 是字典的一个方法，用来更新字典内容（已经存在的键值对进行替换，不存在的键值对进行增加）
        return render(request, self.template_name, context=context)