from django.shortcuts import render

# Create your views here.

# 业务逻辑


from django.http import HttpResponse



def index1(request):
    return HttpResponse("<h1>测试页面1</h1>")

def index2(request):
    return HttpResponse("<h1>测试页面2</h1>")

