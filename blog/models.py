from django.db import models

# Create your models here.

# 数据管理：和数据库打交道写在model里

class Article(models.Model):
    title = models.CharField(max_length=32, default="title")
    content = models.TextField(null=True)