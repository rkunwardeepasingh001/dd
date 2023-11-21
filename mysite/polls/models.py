from django.db import models

# Create your models here.

class User1(models.Model):
  name=models.CharField(max_length=50)
class User2(models.Model):
  s_name=models.CharField(max_length=100)