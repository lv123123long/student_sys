"""
WSGI config for student_sys project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_sys.settings")
profile = os.environ.get('STUDENT_SYS_PROFILE', 'develop')
# 这行代码是从环境变量中获取名为 'STUDENT_SYS_PROFILE' 的值，如果环境变量中没有设置该值，则默认为 'develop'。
# os.environ.get() 方法用于获取环境变量的值，第一个参数是要获取的环境变量的键，第二个参数是可选的默认值。
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings.%s" % profile)
# 这行代码是设置 Django 的配置模块（settings module）。os.environ.setdefault() 方法用于设置环境变量的默认值

application = get_wsgi_application()
