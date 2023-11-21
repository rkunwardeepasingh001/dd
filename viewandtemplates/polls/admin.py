from django.contrib import admin
from .models import Question
class QuestonAdmin(admin.ModelAdmin):
  list_display=['question_text','pub_date']
admin.site.register(Question,QuestonAdmin)


# Register your models here.
