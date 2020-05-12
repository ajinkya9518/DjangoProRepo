from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=30)
    hobby = models.CharField(max_length=30)
    weight = models.IntegerField()
    height = models.IntegerField()
    health = models.CharField(max_length=30)

    def __str__(self):
        return self.name
