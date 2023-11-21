from django.db import models
class Author(models.Model):
  name=models.CharField(max_length=200)
class Book(models.Model):
  title=models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)  
  # Create your models here.
class User(models.Model):
  username=models.CharField(max_length=200)
  user_id=models.IntegerField()
class User_profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='User_profile')
  bio=models.TextField()
class Actor(models.Model):  
  name = models.CharField(max_length=100)  
class Movie(models.Model):  
  title = models.CharField(max_length=100)  
  actors = models.ManyToManyField(Actor)  