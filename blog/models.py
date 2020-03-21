from django.db import models


# Create your models here.

# 数据管理：和数据库打交道写在model里

class Article_aa(models.Model):
    title = models.CharField(max_length=32, default="title")
    content = models.TextField(max_length=64, default="content")
    pub_time = models.DateTimeField(null=True)
    # 修改数据默认显示名称：
    def __unicode__(self):
        return self.title