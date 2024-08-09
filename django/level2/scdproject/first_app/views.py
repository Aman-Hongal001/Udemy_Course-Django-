from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>This is views.py <h1>")

def home(request):
    note = {'ind':"This is inside home function in views.py"}
    return render(request,'index.html',context=note)