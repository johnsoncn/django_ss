"""

这是把工程文件里的 urls.py 模块直接复制过来
"""

from django.conf.urls import url
from blog.views import index1,index2,index3,page
from django.urls import path

app_name = 'blog'

urlpatterns = [
    url(r'test1/', index1),
    url(r'test2/', index2),
    url(r'test3/', index3),
    # 配置跳转路径
    # 应用的url()的第三个参数位置，name='page' （url链接名）
    url(r'article/', page, name='page_aa'),
    # path('article/<page_id>', page, name='page'),

]


"""
python manage.py runserver

http://127.0.0.1:8000/blogtest/test1/
http://127.0.0.1:8000/blogtest/test2/
"""

"""
记住，浏览器要输入的是逗号前面的部分（如test1）
"""