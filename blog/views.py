from django.shortcuts import render

# Create your views here.

# 业务逻辑


from django.http import HttpResponse



def index1(request):
    return HttpResponse("<h1>测试页面1</h1>")

def index2(request):
    return HttpResponse("<h1>测试页面2</h1>")

def index3(request):   # 传输字典参数 title，则把值johnson传过去
    return render(request, 'blog/index.html', {'title':'johnson'})

