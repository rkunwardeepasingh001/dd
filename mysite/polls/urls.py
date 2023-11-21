from django.urls import path 
from .import views

urlpatterns = [
    path("index/",views.index),
    path("<int:question_id>/detail/", views.detail, name="detail"),
    path("<slug:question_id>/result/",views.result,name="result"),
]