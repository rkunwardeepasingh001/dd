from django.db import models
class Data(models.Model):
  ids=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100)
  mob=models.IntegerField()
  email=models.EmailField()
  password=models.CharField(max_length=100)

# Create your models here.
