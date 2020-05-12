from django.db import models

# Create your models here.
class Newspaper(models.Model):
    name = models.CharField(max_length=30)
    fyear = models.IntegerField()
    rate = models.IntegerField()
    language = models.CharField(max_length=30)
    nid = models.IntegerField()

    def __str__(self):
        return self.name
