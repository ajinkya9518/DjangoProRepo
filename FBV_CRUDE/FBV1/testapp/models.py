from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=30)
    eid = models.IntegerField()
    esal = models.IntegerField()
    eaddr = models.CharField(max_length=30)

    def __str__(self):
        return self.ename
