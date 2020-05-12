from django.db import models

# Create your models here.
class Mobile(models.Model):
    mid = models.IntegerField()
    mname = models.CharField(max_length=30)
    mprice = models.IntegerField()
    mbaterry = models.IntegerField()
    mcom = models.CharField(max_length=30)

    def __str__(self):
        return self.mname
