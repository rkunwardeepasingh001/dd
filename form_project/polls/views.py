from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
# def index(request):
#   return HttpResponse("hello server:-")
# def detail(request, question_id):
#   return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#   response = "You're looking at the results of question %s."
#   return HttpResponse(response % question_id)

# def vote(request, question_id):
#   return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.


def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:8]
  # output = ", ".join([q.question_text for q in latest_question_list])
  # return HttpResponse(output)
  # template = loader.get_template("polls/index.html")
  context = {
        "latest_question_list": latest_question_list,
  }
  # print(template)}
  return render(request,'polls/index.html',context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/detail.html", {"question": question})
