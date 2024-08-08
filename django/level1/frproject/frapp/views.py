from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("This is from http response")

def index(request):
    my_dict = {'home':"Inside the Home"}
    return render(request,'index.html',context = my_dict)
