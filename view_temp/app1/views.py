from django.shortcuts import render
from django.http import HttpResponse
def func(request):
  c_nm={'cname':'django'}
  return render(request,'page1.html',c_nm)
def func1(request):
  return HttpResponse("hello fromm app1:-")
def func2(request):
  return render(request,'page1.html')
# Create your views here.
