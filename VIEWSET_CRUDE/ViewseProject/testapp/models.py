from django.db import models

# Create your models here.
class Students(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=30)
    smarks = models.IntegerField()
    saddr = models.CharField(max_length=30)

    def __str__(self):
        return self.sname
