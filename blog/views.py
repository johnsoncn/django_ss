from django.shortcuts import render

# Create your views here.

# 业务逻辑


from django.http import HttpResponse


def index(request):
    # 返回字符
    return HttpResponse('hello, blog1111')

