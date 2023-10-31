#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：base_admin.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/11/1 0:27 
'''
from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. 用来处理文章、分类、标签、侧边栏、友链这些model的owner字段自动补充
    2. 用来针对queryset过滤当前用户的数据
    """
    exclude = ('owner', )

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        # request：就是当前请求，request.user 就是当前登录用户
        # 通过传递obj.owner ， 就能达到自动设置owner的目的
        # form 就是页面提交过来的表单的对象
        # change：用于标志本次保存的数据是新增的，还是更新的
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
    # 重写ModelAdmin的save_model 方法，作用是：保存数据到数据库中