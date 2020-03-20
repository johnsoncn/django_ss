"""

这是把工程文件里的 urls.py 模块直接复制过来
"""

from django.conf.urls import url
from blog.views import index1,index2,index3

urlpatterns = [
    url(r'test1/', index1),
    url(r'test2/', index2),
    url(r'test3/', index3),
]


"""
python manage.py runserver

http://127.0.0.1:8000/myAPP/test1/
http://127.0.0.1:8000/myAPP/test2/
"""
