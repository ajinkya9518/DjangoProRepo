from django.db import models

# Create your models here.
class Newspaper(models.Model):
    nid = models.IntegerField()
    name = models.CharField(max_length = 30)
    ceo = models.CharField(max_length=30)

    def __str__(self):
        return self.name
