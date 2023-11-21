from django.contrib import admin
from .models import Empreg
class EmpAdmin(admin.ModelAdmin):
  list_display=['ename','emob']
admin.site.register(Empreg,EmpAdmin)
# Register your models here.
