#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/10/29 21:10 
'''
from django.conf.urls import url
from django.contrib import admin

from student.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # as_view()其实是对get和post方法的一个包装。里面做的事情，你可以简单的理解为我们上一节中自己写的判断request.method的逻辑。,,是继承类里面的方法
    url(r'^admin/', admin.site.urls),
]