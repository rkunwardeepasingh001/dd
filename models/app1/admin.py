from django.contrib import admin
from app1.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
  list_display=['empid','empname','last_modified','date_last_modified','img','email','emp_txt']
admin.site.register(Employee,EmployeeAdmin)
# admin.site.register(Employee)

# Register your models here.
