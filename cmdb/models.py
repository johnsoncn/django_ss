from django.db import models

# Create your models here.


# 自己先创建一个host表
class host(models.Model):
    ip = models.GenericIPAddressField(max_length=60)
    name = models.CharField(max_length=50)
    class _Meta():
        pass
    def __unicode__(self):
        return self.ip