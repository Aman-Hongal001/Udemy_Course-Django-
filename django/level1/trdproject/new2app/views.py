from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Template Problem Solution Page</em>")

def help(request):
    help_dict = {'help':"This is mine Help page"}
    return render(request,'index.html',context = help_dict)