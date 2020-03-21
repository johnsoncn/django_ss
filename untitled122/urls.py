"""untitled122 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# URL配置文件
# django项目中所有地址（页面）都需要我们自己去配置其URL

from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
import blog.views as bl

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'blogindex/', bl.index, name="index11"),
    # url(r'opinion/', include('opinion_app.urls')),

    # 用include管理blog里的所有urls
    # 根urls中，写在include()的第二个参数位置，namespace='blog' （这个应用的命名空间）
    url('blogtest/', include('blog.urls', namespace='blog_aa')),
]