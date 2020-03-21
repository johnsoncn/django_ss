from django.contrib import admin
from . import models

# Register your models here.

# 后台管理，连一些数据、页面转线
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','pub_time')

admin.site.register(models.Article_aa, ArticleAdmin)
