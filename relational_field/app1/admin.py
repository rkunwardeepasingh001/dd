from django.contrib import admin
from app1.models import Author,Book,User,User_profile,Actor,Movie
class Author_admin(admin.ModelAdmin):
  list_display=['name']
admin.site.register(Author,Author_admin)
class Book_admin(admin.ModelAdmin):
  list_display=['title','author']
admin.site.register(Book,Book_admin)
class User_admin(admin.ModelAdmin):
  list_display=['username']
admin.site.register(User,User_admin)
class User_profile_admin(admin.ModelAdmin):
  list_display=['user','bio']
admin.site.register(User_profile,User_profile_admin)
class Actor_admin(admin.ModelAdmin):
  list_display=['name']
admin.site.register(Actor,Actor_admin)
class Movie_admin(admin.ModelAdmin):
  list_display=['title']
admin.site.register(Movie,Movie_admin)