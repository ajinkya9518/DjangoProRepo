from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    marks = models.FloatField()
    addr = models.TextField()
    emp_img = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = "employee"
