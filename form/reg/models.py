from django.db import models
class Empreg(models.Model):
  ename=models.CharField(max_length=100)
  emob=models.IntegerField()
# Create your models here.
