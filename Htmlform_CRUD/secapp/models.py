from django.db import models

# Create your models here.
class State(models.Model):
    statename=models.CharField(max_length=30)
    statecode=models.IntegerField()
    state_cm=models.CharField(max_length=40)

    def __str__(self):
        return self.statename
    class Meta:
        db_table="state"