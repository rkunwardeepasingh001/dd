from django.db import models
class Employee(models.Model):
  empid= models.AutoField(primary_key=True)
  empname= models.CharField(max_length=500)
  last_modified = models.DateTimeField(auto_now_add=True)
  date_last_modified = models.DateField(default=None)
  img = models.ImageField(null=True,blank=True)
  email=models.EmailField(max_length=250)
  emp_txt=models.TextField()
  # def __str__(self):
  #   return self.empid
# Create your models here.
