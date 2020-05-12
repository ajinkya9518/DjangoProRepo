from django.db import models

# Create your models here.
class City(models.Model):
    cname = models.CharField(max_length=30)
    ccode = models.CharField(max_length=30)
    crank = models.IntegerField()
