from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse("hello,Server")
def detail(request,question_id):
  return HttpResponse("hello,from detail,ques_id= %s." %question_id)
def result(request,question_id):
  response="hello,from result ,ques_id=%s"
  return HttpResponse(response %question_id)