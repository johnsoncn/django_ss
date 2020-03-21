from django.shortcuts import render

# Create your views here.

# 业务逻辑


from django.http import HttpResponse
from blog import models

"""
也就是把数据库 models.py，和前端界面index.html  关联起来，做信息传输
"""

def index1(request):
    return HttpResponse("<h1>测试页面1</h1>")

def index2(request):
    return HttpResponse("<h1>测试页面2</h1>")

def index3(request):
    articles_aa = models.Article_aa.objects.all()  # 从blog.models里导入Article_aa方法  （导入数据库）
    return render(request, 'blog/index.html', {'articles':'articles_aa'})  # 然后把 articles(key) 提供给前端的

def page(request):
    articles_bb = models.Article_aa.objects.get(pk=1)
    # articles_bb = models.Article_aa.objects.get(pk=articleID)
    return render(request, 'blog/article_page.html', {'article_Redir':'articles_bb'})

def edit_action(request):
    # 拿到title和content
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    # 保持title和content
    models.Article_aa.objects.create(title=title, content=content)
    articles = models.Article_aa.objects.all()
    return render(request, 'blog/index.html', {'articles': 'articles'})
