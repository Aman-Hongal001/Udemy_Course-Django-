from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert':"Hello I am in view.py"}
    return render(request,'index.html',context=my_dict)

def nextpage(request):
    return HttpResponse("<h1><em>This is mine HTTP Response</em></h1>")