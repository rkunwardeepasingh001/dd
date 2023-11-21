from django.urls import path
from . import views
urlpatterns = [
  path('func/',views.func),
  path('func1/',views.func1),
  path("func2/",views.func2)
  
]