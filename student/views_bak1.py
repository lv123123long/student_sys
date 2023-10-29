# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# 使用django提供的render() 方法来渲染页面





def index(request):
    words = 'World!'
    return render(request, 'index.html', context={'words': words})

    # 第一个参数是请求的页面地址，django会去每个app的templates下面进行寻找，顺序查找（如果两个app有相同的html页面，会加载前面那个）
    # 第二个context 是替换参数的操作，将html页面的words 替换成 World!
