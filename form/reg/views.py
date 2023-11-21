from django.shortcuts import render , HttpResponse
from reg.form import RegForm
def reg1(request):
  r1=RegForm()
  Reg_data={'form':r1}
  return render(request,'reg.html',Reg_data)
# # Create your views here.
# def reg1(request):
#   if request.method=="post":
#     r1=RegForm(request.POST)
#     if r1.is_valid():
#       return HttpResponse("jhgjh hghbvh ")
#     else:
#       r1=RegForm()
#     # Reg_data={'form':r1}
#     return render(request,'reg.html',)