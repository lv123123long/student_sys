# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="电话")

    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name="审核状态")
    # 带有choices属性的字段时，Django会自动帮我们调用get_status_display方法
    # 而在我们自己写的模板中，我们需要自己来写。并且在模板中不支持函数/方法调用，你只需要写方法名称即可，后面的括号不需要写。Django会自行帮你调用(如果是方法的话)。


    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    def __unicode__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"