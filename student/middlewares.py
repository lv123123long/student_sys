#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student_sys 
@File    ：middlewares.py
@IDE     ：PyCharm 
@Author  ：lvlongxin
@Date    ：2023/10/29 21:12 
'''
import time

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

# 类的作用：统计首页每次访问所消耗的时间，也就是wsgi接口或者socket接口接到请求，到最终返回的时间
class TimeItMiddleware(MiddlewareMixin):
    # 列出了一个Middleware的完整接口
    def process_request(self, request):
        # 一个请求到middleware层，进入第一个方法，一般可以在这里做一个校验，比如用户登录，http中是否有认证头之类的验证
        # 这个方法需要两个返回值， HttpResponse或者None，
        # 如果返回HttpResponse，那么接下来的处理方法只会执行process_response，其他的方法将不会被执行
        # 需要注意的是，如果你的middleware在settings配置的MIDDLEWARE_CLASS的第一个的话，那么剩下的middleware也不会被执行。
        # 另外一个返回值是None，如果返回None，那么Django会继续执行其他的方法。
        return

    def process_view(self, request, func, *args, **kwargs):
        # 这个方法是在process_request之后执行的
        # func：就是我们要执行的view方法
        # 返回值也是两个HttpResponse和None
        # 逻辑也是一样。如果返回None，那么Django会帮你执行view函数，从而得到最终的Response。
        if request.path != reverse('index'):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('{:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        # 只有在发生异常时，才会进入到这个方法。
        # 哪个阶段发生的异常呢？可以简单的理解为在将要调用的view中出现异常（就是在process_view的func函数中）或者返回的模板Response在render时发生的异常，会进入到这个方法中。
        # 但是需要注意的是，如果你在process_view中手动调用了func，就像我们上面做的那样，那就不会触发process_exception了。
        # 这个方法接收到异常之后，可以选择处理异常，然后返回一个含有异常信息的HttpResponse，或者直接返回None，不处理，这种情况Django会使用自己的异常模板。
        pass

    def process_template_response(self, request, response):
        # 执行完上面的方法，并且Django帮忙我们执行完view之后，拿到最终的response，
        # 如果是使用了模板的Response(是指通过return render(request, 'index.html', context={})的方式返回Response，就会来到这个方法中。
        # 这个方法中我们可以对response做一下操作，比如Content-Type设置，或者其他HEADER的修改/增加。
        return response

    def process_response(self, request, response):
        # 当所有流程都处理完毕，就来到了这个方法，这个方法的逻辑跟process_template_response是完全一样的。
        # 只是process_template_response是针对带有模板的response的处理。
        return response