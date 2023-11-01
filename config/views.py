from django.http import HttpResponse


def links(request):
    return HttpResponse('links')
# 这里就是返回简单的字符串就可以，links的url定义中，没有任何参数，所以这里也不需要定义除了request之外的参数